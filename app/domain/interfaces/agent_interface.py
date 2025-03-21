from abc import ABC, abstractmethod
from app.domain.models.request import Request
from app.domain.models.response import Response

class AgentInterface(ABC): ##todo: not sure if Agent should handle requests. Maybe it should be only responsible for business logic and request agnostic.
    @abstractmethod
    def handle(self, req: Request, query: str) -> Response:
        pass
