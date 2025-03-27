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
        self.tools = {}

    def prepare_context(self, objective: str, data: any, params: dict) -> str:

        self.logger.debug(f"Tools: {self.tools}")

        tags = params.get("tags", [])
        #self.logger.debug(f"Tags: {tags}")

        if data and data.get("file_name"): ## Bad way to handle file upload
            self.logger.debug(f"File Name: {data.get('file_name')}")
            self.logger.debug(f"File Content Type: {data.get('content_type')}")

            ocr_tool = self.tools["ocr"]
            ocr_result = ocr_tool.execute(data)
            self.logger.debug(f"OCR Result: {ocr_result}")
            #return ocr_result
            return f"**Document:** {ocr_result} \n\n **Tags:** {tags}"
    
        return "\n".join(self._search_vector_store(objective, data, params))
    
    def _search_vector_store(self, objective: str, data: any, params: dict) -> list:
        """
        Prepare context for the agent. Here you can add any logic to prepare context for the agent.
        Such as parse and prepare data, use additional params, etc.
        """

        ## example
        self.logger.debug(params.get("user_id", "no user id"))

        embedding = self.embedder.embed_texts([objective])[0]
        return self.vector_store.search_similar(embedding, params.get("top_k", 5))