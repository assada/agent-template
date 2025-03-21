class Response:
    def __init__(self, success: bool, result=None, error="", status_code=200):
        self.success = success
        self.result = result
        self.error = error
        self.status_code = status_code
