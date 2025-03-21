from typing import List
import chromadb
from chromadb.config import Settings
from app.config import Config
from app.domain.interfaces.vector_store_interface import VectorStoreInterface

class ChromaVectorStore(VectorStoreInterface):
    def __init__(self):
        self.client = chromadb.Client(Settings(
        chroma_api_impl="chromadb.api.fastapi.FastAPI",
        chroma_server_host=Config.CHROMA_SERVER_HOST,
        chroma_server_http_port=int(Config.CHROMA_SERVER_PORT)
    ))
        self.collection = self.client.get_or_create_collection("default_collection")

    def add_embeddings(self, embeddings: list[list[float]], documents: list[str]) -> None:
        ids = [str(i) for i in range(len(documents))]
        self.collection.add(embeddings=embeddings, documents=documents, ids=ids)

    def similarity_search(self, query_embedding: list[float], k: int) -> list[str]:
        results = self.collection.query(query_embeddings=[query_embedding], n_results=k)
        return results["documents"][0] if "documents" in results else []

    def delete_documents(self, document_ids: List[str]) -> None:
        self.collection.delete(where={"id": {"in": document_ids}})

    def update_embeddings(self, document_ids: List[str], embeddings: List[List[float]], documents: List[str]) -> None:
        self.collection.update(ids=document_ids, embeddings=embeddings, documents=documents)
