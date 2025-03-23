class ToolInterface:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def execute(self, input: any) -> str:
        pass

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def self_describe(self) -> str:
        return f"{self.name}: {self.description}"