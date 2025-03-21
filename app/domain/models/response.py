class Response:
    def __init__(self, success: bool, result=None, error=""):
        self.success = success
        self.result = result
        self.error = error
