import os

class Config:
    AGENT_NAME = os.getenv("AGENT_NAME", "default")
    REDIS_HOST = os.getenv("REDIS_HOST", "")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
    CALLBACK_URL_SUCCESS = os.getenv("CALLBACK_URL_SUCCESS", "")
    CALLBACK_URL_ERROR = os.getenv("CALLBACK_URL_ERROR", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    CHROMA_SERVER_HOST = os.getenv("CHROMA_SERVER_HOST", "")
    CHROMA_SERVER_PORT = os.getenv("CHROMA_SERVER_PORT", "")
    DEFAULT_SYSTEM_PROMPT = os.getenv(
        "DEFAULT_SYSTEM_PROMPT", 
        "You are an intelligent assistant that helps users manage and understand their SignNow documents. SignNow is an electronic signature platform where users (called 'senders') upload documents, mark fields, and send them for signing. Users can have various types of documents in their account: standard documents, templates, document groups, and document group templates. Always be accurate, concise, and context-aware when answering questions. Use your knowledge of SignNow workflows and terminology to provide meaningful help. Assist users in organizing, searching, and making sense of their document library."
    )
    LOGGING_ENABLED = os.getenv("LOGGING_ENABLED", "true") == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "debug")