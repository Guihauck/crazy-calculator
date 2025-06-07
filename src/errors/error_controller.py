from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_content import HttpUnprocessableContentError 
from typing import Dict

def HandlerError(error: Exception) -> Dict:
    if isinstance(error, (HttpBadRequestError, HttpUnprocessableContentError)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        }
    
    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    }