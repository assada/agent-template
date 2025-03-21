from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> dict:
        """
        Generate json response using the LLM.
        """
        pass
