from app.services.vector_store_service import VectorStoreService
from app.infrastructure.openai_embedder import OpenAIEmbedder

def run():
    texts = ["Document one", "Document two", "Document three", "Document four", "Document five", "strings sting"]
    embeddings = OpenAIEmbedder().embed_texts(texts)
    VectorStoreService().add_data(embeddings, texts)

if __name__ == "__main__":
    run()
