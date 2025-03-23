import json
from app.domain.interfaces.agent_interface import AgentInterface
from app.domain.models.agent_result import AgentResult
from app.services.llm_service import LLMService
from app.services.vector_store_service import VectorStoreService
from app.infrastructure.openai_embedder import OpenAIEmbedder
from app.services.prompt_service import PromptService
from app.config import Config
from typing import Optional

from app.utils.logger import Logger

class DefaultAgent(AgentInterface):
    def __init__(self, agent_name: str, prompt_service: Optional[PromptService] = None, llm: Optional[LLMService] = None):
        self.llm = llm or LLMService()
        self.vector_store = VectorStoreService()
        self.embedder = OpenAIEmbedder()
        self.prompt_service = prompt_service or PromptService()
        self.agent_name = agent_name
        self.logger = Logger(self.agent_name)
        
    def handle(self, query: str, data: any, params: dict) -> AgentResult:
        try:
            context = self._prepare_context(query, data, params)
            if not context or len(context) == 0:
                return AgentResult(False, "Can't build context")
            self.logger.debug(context)

            prompt = self.prompt_service.format_prompt(context, query, Config.DEFAULT_SYSTEM_PROMPT)
            self.logger.debug(prompt)

            answer = self.llm.generate(prompt)
            self.logger.debug(answer)
            
            return AgentResult(True, json.loads(answer.get("content")))
        except Exception as e:
            self.logger.error(e, exc_info=True)

            return AgentResult(False, str(e))
        
    def _prepare_context(self, query: str, data: any, params: dict) -> list:
        """
        Prepare context for the agent. Here you can add any logic to prepare context for the agent.
        Such as parse and prepare data, use additional params, etc.
        """
        embedding = self.embedder.embed_texts([query])[0] ## todo: return list of embeddings? need to investigate
        return self.vector_store.search_similar(embedding, params.get("top_k", 5))
