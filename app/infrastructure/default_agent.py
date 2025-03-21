from app.domain.interfaces.agent_interface import AgentInterface
from app.domain.models.request import Request
from app.domain.models.response import Response
from app.services.llm_service import LLMService
from app.services.vector_store_service import VectorStoreService
from app.infrastructure.openai_embedder import OpenAIEmbedder
from app.services.prompt_service import PromptService
from app.config import Config
from typing import Optional

class DefaultAgent(AgentInterface):
    def __init__(self, prompt_service: Optional[PromptService] = None, llm: Optional[LLMService] = None):
        self.llm = llm or LLMService()
        self.vector_store = VectorStoreService()
        self.embedder = OpenAIEmbedder()
        self.prompt_service = prompt_service or PromptService()

    def handle(self, req: Request, query: str) -> Response:
        try:
            embedding = self.embedder.embed_texts([query])[0] ## todo: return list of embeddings? need to investigate
            context = self.vector_store.search_similar(embedding, 0.7) ## todo: process all embeddings? need to investigate

            prompt = self.prompt_service.format_prompt(context, query, Config.DEFAULT_SYSTEM_PROMPT)

            answer = self.llm.generate(prompt)
            return Response(True, {"answer": answer, "data": req.data, "params": req.params}, "")
        except Exception as e:
            return Response(False, None, str(e))
