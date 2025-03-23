from app.domain.interfaces.agent_interface import AgentInterface
from app.infrastructure.default_agent import DefaultAgent
from app.domain.models.request import Request
from app.domain.models.response import Response

class AgentService:
    def __init__(self, agent: AgentInterface):
        self.agent = agent or DefaultAgent("DefaultAgent")

    def handle(self, req: Request) -> Response:
        result = self.agent.handle(req.query, req.data, req.params)
        return result.to_response()
