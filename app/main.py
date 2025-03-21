from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
    query: str ##todo: not sure if this is needed. Looks like agent dont want handle custom query.
    data: dict | None = None ##todo: data can be a file or json object.
    params: dict | None = None ##todo: i think this is should be also dataclass.

@app.post("/process")
def process_endpoint(body: RagRequestModel):
    res = AgentService().handle(Request(body.query, body.data, body.params))
    return {"success": res.success, "result": res.result, "error": res.error} ##todo: need error handling. and do not return 200 status code if error.
