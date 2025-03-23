from typing import Any, Dict, Optional
from fastapi import Depends, FastAPI, Form, HTTPException, Response, UploadFile, File, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ValidationError
from fastapi.encoders import jsonable_encoder
from app.config import Config
from app.infrastructure.chroma_vector_store import ChromaVectorStore
from app.infrastructure.default_agent import DefaultAgent
from app.infrastructure.default_context_builder import DefaultContextBuilder
from app.infrastructure.default_prompt_formatter import DefaultPromptFormatter
from app.infrastructure.openai_embedder import OpenAIEmbedder
from app.infrastructure.openai_llm import OpenAILLM
from app.infrastructure.tools.ocr import OCRTool
from app.services.agent_service import AgentService
from app.domain.models.request import Request
from dotenv import load_dotenv

from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from app.services.vector_store_service import VectorStoreService

load_dotenv() ## load environment variables for local development. not needed for docker.

app = FastAPI(
    title="Agent Template",
    description="Template for creating agents",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RagRequestModel(BaseModel):
    objective: str = Field(..., description="Main objective of the agent")
    params: Optional[Dict[str, Any]] = Field(None, description="Additional parameters for the agent")

def checker(data: str = Form(...)):
    try:
        return RagRequestModel.model_validate_json(data)
    except ValidationError as e:
        raise HTTPException(
            detail=jsonable_encoder(e.errors()),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )

##{"objective": "What is this document about?"}
##{"objective": "Based on document content chose best 3 tags for this documents. Response in json format!", "params": {"tags": ["personal", "purchases", "customs", "work", "unread", "important", "not-important"]}}
@app.post("/process")
async def process_endpoint(response: Response, body: RagRequestModel = Depends(checker), file: Optional[UploadFile] = File(None)):
    prompt_service = PromptService(DefaultPromptFormatter())
    llm = LLMService(OpenAILLM())
    context_builder = DefaultContextBuilder(VectorStoreService(ChromaVectorStore()), OpenAIEmbedder())
    tools = {
        "ocr": OCRTool()
    }
    agent = DefaultAgent(Config.AGENT_NAME, prompt_service, llm, context_builder, tools)

    request_data = {}
    if file:
        file_content = await file.read()
        request_data = {
            "file_name": file.filename,
            "file_content": file_content,
            "content_type": file.content_type
        }
    
    res = AgentService(agent).handle(Request(body.objective, request_data, body.params))
    response.status_code = res.status_code or 200
    return {"success": res.success, "result": res.result, "error": res.error}
