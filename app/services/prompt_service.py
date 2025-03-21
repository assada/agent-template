from app.domain.interfaces.prompt_interface import PromptInterface
from app.infrastructure.default_prompt_formatter import DefaultPromptFormatter

class PromptService:
    def __init__(self, prompt_formatter: PromptInterface = None):
        self.prompt_formatter = prompt_formatter or DefaultPromptFormatter()
    
    def format_prompt(self, context: list[str], query: str, system_prompt: str = None) -> str:
        return self.prompt_formatter.generate_prompt(context, query, system_prompt)