from abc import ABC, abstractmethod

class PromptInterface(ABC):
    @abstractmethod
    def generate_prompt(self, context: str, objective: str, system_prompt: str) -> str:
        pass
