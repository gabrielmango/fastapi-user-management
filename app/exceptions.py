"""File responsible for HTTP errors."""
from fastapi import HTTPException


class HttpError(HTTPException):
    """Custom HTTP error class."""

    @staticmethod
    def user_already_exists(message: str = 'User already exists'):
        """Return HTTP 400 Bad Request error with user already exists message."""
        raise HttpError(status_code=400, detail=message)

    @staticmethod
    def bad_request(message: str = 'Invalid request'):
        """Return HTTP 400 Bad Request error with invalid request message."""
        raise HttpError(status_code=400, detail=message)
