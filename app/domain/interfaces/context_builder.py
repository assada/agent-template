from app.domain.models.request import Request

class ContextBuilderInterface:
    def prepare_context(self, query: str, data: any, params: dict) -> str:
        pass
