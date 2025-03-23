class ContextBuilderInterface:
    def __init__(self):
        self.tools = {}

    def prepare_context(self, objective: str, data: any, params: dict) -> str:
        pass

    def set_tools(self, tools: dict):
        self.tools = tools
