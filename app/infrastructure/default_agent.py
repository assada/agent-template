import json
from app.domain.interfaces.agent_interface import AgentInterface
from app.domain.interfaces.context_builder import ContextBuilderInterface
from app.domain.models.agent_result import AgentResult
from app.infrastructure.default_context_builder import DefaultContextBuilder
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from app.config import Config
from typing import Optional

from app.utils.logger import Logger

class DefaultAgent(AgentInterface):
    def __init__(
            self, 
            agent_name: str, 
            prompt_service: Optional[PromptService] = None, 
            llm: Optional[LLMService] = None, 
            context_builder: Optional[ContextBuilderInterface] = None,
            tools: Optional[dict] = None
        ):
        self.llm = llm or LLMService()
        self.prompt_service = prompt_service or PromptService()
        self.context_builder = context_builder or DefaultContextBuilder()
        self.agent_name = agent_name
        self.logger = Logger(self.agent_name)
        self.tools = tools or {}
        self.context_builder.set_tools(self.tools)

    def handle(self, objective: str, data: any, params: dict) -> AgentResult:
        try:
            context = self.context_builder.prepare_context(objective, data, params)
            if not context or len(context) == 0:
                self.logger.warning("Context is empty")
            self.logger.debug(context)

            prompt = self.prompt_service.format_prompt(context, objective, Config.DEFAULT_SYSTEM_PROMPT)
            self.logger.debug(prompt)

            answer = self.llm.generate(prompt)
            self.logger.debug(answer)

            return AgentResult(True, json.loads(answer.get("content")))
        except Exception as e:
            self.logger.error(e, exc_info=True)

            return AgentResult(False, str(e))
