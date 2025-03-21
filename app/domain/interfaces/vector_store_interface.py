from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class VectorStoreInterface(ABC):
    @abstractmethod
    def add_embeddings(self, embeddings: List[List[float]], documents: List[str], metadata: Optional[List[Dict[str, Any]]] = None) -> None:
        pass

    @abstractmethod
    def similarity_search(self, query_embedding: List[float], k: int = 5, filter_criteria: Optional[Dict[str, Any]] = None) -> List[str]:
        pass

    @abstractmethod
    def delete_documents(self, document_ids: List[str]) -> None:
        pass

    @abstractmethod
    def update_embeddings(self, document_ids: List[str], embeddings: List[List[float]], documents: List[str]) -> None:
        pass
