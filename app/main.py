from typing import Any, Dict, Optional
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.config import Config
from app.infrastructure.chroma_vector_store import ChromaVectorStore
from app.infrastructure.default_agent import DefaultAgent
from app.infrastructure.default_context_builder import DefaultContextBuilder
from app.infrastructure.default_prompt_formatter import DefaultPromptFormatter
from app.infrastructure.openai_embedder import OpenAIEmbedder
from app.infrastructure.openai_llm import OpenAILLM
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
    query: str = Field(..., description="User query for the agent to process")
    data: Optional[Dict[str, Any]] = Field(None, description="Data, can be a file or JSON object")
    params: Optional[Dict[str, Any]] = Field(None, description="Additional parameters for the agent")

@app.post("/process")
def process_endpoint(body: RagRequestModel, response: Response):
    prompt_service = PromptService(DefaultPromptFormatter())
    llm = LLMService(OpenAILLM())
    context_builder = DefaultContextBuilder(VectorStoreService(ChromaVectorStore()), OpenAIEmbedder())
    agent = DefaultAgent(Config.AGENT_NAME, prompt_service, llm, context_builder)
    
    res = AgentService(agent).handle(Request(body.query, body.data, body.params))
    response.status_code = res.status_code or 200
    return {"success": res.success, "result": res.result, "error": res.error}
