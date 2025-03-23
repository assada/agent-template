from app.domain.interfaces.prompt_interface import PromptInterface

class DefaultPromptFormatter(PromptInterface):
    def generate_prompt(self, context: str, objective: str, system_prompt: str) -> str:     
        if not system_prompt:
            system_prompt = "You are a helpful assistant that provides accurate answers based on the given context."
            
        prompt = f"""
Your role:
{system_prompt}

Use the following context to enhance your understanding of the objective:
{context}

Objective:
{objective}

The response should be formatted strictly as a JOSN file, following the structure provided below. Do not include any code blocks within the JOSN format.

**Response Format:**
```json
{{
    "answer": <answer to the objective>
}}
```
"""
        return prompt.strip()