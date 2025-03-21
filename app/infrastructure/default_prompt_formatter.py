from app.domain.interfaces.prompt_interface import PromptInterface

class DefaultPromptFormatter(PromptInterface):
    def generate_prompt(self, context: list[str], query: str, system_prompt: str) -> str:
        formatted_context = "\n".join(context)
        
        if not system_prompt:
            system_prompt = "You are a helpful assistant that provides accurate answers based on the given context."
            
        prompt = f"""
{system_prompt}

Context:
{formatted_context}

Query:
{query}
"""
        return prompt.strip()