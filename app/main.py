from typing import Any, Dict, Optional
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.config import Config
from app.services.agent_service import AgentService
from app.domain.models.request import Request
from dotenv import load_dotenv

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
    res = AgentService(Config.AGENT_NAME).handle(Request(body.query, body.data, body.params))
    response.status_code = res.status_code or 200
    return {"success": res.success, "result": res.result, "error": res.error}
