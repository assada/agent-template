class Request:
    def __init__(self, query: str, data=None, params=None):
        self.query = query
        self.data = data
        self.params = params
