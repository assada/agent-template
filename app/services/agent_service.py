from app.infrastructure.default_agent import DefaultAgent
from app.domain.models.request import Request
from app.domain.models.response import Response

class AgentService:
    def __init__(self):
        self.agent = DefaultAgent()

    def handle(self, req: Request) -> Response:
        return self.agent.handle(req, req.query)
