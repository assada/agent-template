from app.domain.interfaces.context_builder import ContextBuilderInterface
from app.domain.interfaces.embeddings_interface import EmbeddingsInterface
from app.services.vector_store_service import VectorStoreService
from app.infrastructure.openai_embedder import OpenAIEmbedder
from app.utils.logger import Logger

class DefaultContextBuilder(ContextBuilderInterface):
    def __init__(self, vector_store: VectorStoreService, embedder: EmbeddingsInterface):
        self.vector_store = vector_store or VectorStoreService()
        self.embedder = embedder or OpenAIEmbedder()
        self.logger = Logger("DefaultContextBuilder")

    def prepare_context(self, query: str, data: any, params: dict) -> str:
        return "\n".join(self._search_vector_store(query, data, params))
    
    def _search_vector_store(self, query: str, data: any, params: dict) -> list:
        """
        Prepare context for the agent. Here you can add any logic to prepare context for the agent.
        Such as parse and prepare data, use additional params, etc.
        """

        ## example
        self.logger.debug(params.get("user_id", "no user id"))

        embedding = self.embedder.embed_texts([query])[0]
        return self.vector_store.search_similar(embedding, params.get("top_k", 5))