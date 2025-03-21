from app.domain.interfaces.llm_interface import LLMInterface
from app.infrastructure.openai_llm import OpenAILLM

class LLMService:
    def __init__(self, llm: LLMInterface = None):
        self.llm = llm or OpenAILLM()

    def generate(self, prompt: str) -> str:
        return self.llm.generate_text(prompt)
