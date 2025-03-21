from abc import ABC, abstractmethod

class PromptInterface(ABC):
    @abstractmethod
    def generate_prompt(self, context: list[str], query: str, system_prompt: str) -> str:
        pass
