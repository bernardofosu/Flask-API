class CustomError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.status = 'fail' if 400 <= status_code < 500 else 'error'
        self.is_operational = True