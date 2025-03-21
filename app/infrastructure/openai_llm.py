import openai
from langchain_openai import ChatOpenAI
from app.config import Config
from app.domain.interfaces.llm_interface import LLMInterface

class OpenAILLM(LLMInterface):
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.model = ChatOpenAI(temperature=0, model=Config.OPENAI_MODEL)

    def generate_text(self, prompt: str) -> dict:
        return self.model.invoke(prompt).model_dump()
