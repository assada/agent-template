import openai
from langchain_community.embeddings import OpenAIEmbeddings ## langchain_openai import OpenAIEmbeddings
from app.config import Config
from app.domain.interfaces.embeddings_interface import EmbeddingsInterface

class OpenAIEmbedder(EmbeddingsInterface):
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY
        self.embedder = OpenAIEmbeddings()

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return self.embedder.embed_documents(texts)
