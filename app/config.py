import os

class Config:
    AGENT_NAME = os.getenv("AGENT_NAME", "default")
    REDIS_HOST = os.getenv("REDIS_HOST", "")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
    CALLBACK_URL_SUCCESS = os.getenv("CALLBACK_URL_SUCCESS", "")
    CALLBACK_URL_ERROR = os.getenv("CALLBACK_URL_ERROR", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    CHROMA_SERVER_HOST = os.getenv("CHROMA_SERVER_HOST", "")
    CHROMA_SERVER_PORT = os.getenv("CHROMA_SERVER_PORT", "")
    DEFAULT_SYSTEM_PROMPT = os.getenv(
        "DEFAULT_SYSTEM_PROMPT", 
        "You are a helpful assistant that provides accurate and relevant information based on the provided context."
    )
    LOGGING_ENABLED = os.getenv("LOGGING_ENABLED", "true") == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "debug")