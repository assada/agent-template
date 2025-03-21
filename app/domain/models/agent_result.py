from app.domain.models.response import Response


class AgentResult:
    def __init__(self, success: bool, result=None):
        self.success = success
        self.result = result

    def to_response(self) -> Response:
        if not self.success:
            return Response(False, None, self.result, 500)

        return Response(self.success, self.result)
