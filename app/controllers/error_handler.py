from flask import jsonify

class CustomError(Exception):
    def __init__(self, message, status_code=400, status='fail'):
        super().__init__(message)
        self.status_code = status_code
        self.status = status

# ✅ Global error handler function (OUTSIDE the class)
def global_error_handler(error):
    """Handles CustomError globally and returns a JSON response"""
    response = {
        "status": error.status,
        "message": str(error)
    }
    return jsonify(response), error.status_code
