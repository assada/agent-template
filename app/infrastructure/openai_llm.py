import openai
from langchain_community.chat_models import ChatOpenAI
from app.config import Config
from app.domain.interfaces.llm_interface import LLMInterface

class OpenAILLM(LLMInterface):
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.model = ChatOpenAI(temperature=0, model="gpt-4o-mini") ## Todo: add model to config

    def generate_text(self, prompt: str) -> str:
        return self.model(prompt).content
