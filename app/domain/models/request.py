class Request:
    def __init__(self, objective: str, data=None, params=None):
        self.objective = objective
        self.data = data
        self.params = params
