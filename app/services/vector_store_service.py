from app.domain.interfaces.vector_store_interface import VectorStoreInterface
from app.infrastructure.chroma_vector_store import ChromaVectorStore

class VectorStoreService:
    def __init__(self, store: VectorStoreInterface = None):
        self.store = store or ChromaVectorStore()

    def add_data(self, embeddings: list[list[float]], texts: list[str]) -> None:
        self.store.add_embeddings(embeddings, texts)

    def search_similar(self, query_embedding: list[float], k: int) -> list[str]:
        return self.store.similarity_search(query_embedding, k)
