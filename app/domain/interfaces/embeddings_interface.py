from abc import ABC, abstractmethod

class EmbeddingsInterface(ABC):
    @abstractmethod
    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        pass
