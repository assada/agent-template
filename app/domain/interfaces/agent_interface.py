from abc import ABC, abstractmethod
from app.domain.models.agent_result import AgentResult

class AgentInterface(ABC):
    @abstractmethod
    def handle(self, query: str, data: any, params: dict) -> AgentResult:
        pass
