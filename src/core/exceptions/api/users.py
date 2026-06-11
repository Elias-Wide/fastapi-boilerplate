from fastapi import status

from src.core.exceptions.api.base import APIException


class UserAPIException(APIException):
    """Base HTTP exception dedicated to the user module."""

    def __init__(
        self,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        detail: str = 'User service error.',
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)


class UserConflictAPIException(UserAPIException):
    """HTTP 400 exception for conflicting user registration data."""

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with these credentials already exists.',
        )


class UserNotFoundAPIException(UserAPIException):
    """HTTP 404 exception when a user resource is missing."""

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found.',
        )


class UnauthorizedAPIException(UserAPIException):
    """HTTP 401 exception for wrong credentials or broken sessions."""

    def __init__(self, detail: str = 'Invalid username or password.') -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        )


class TokenExpiredAPIException(UserAPIException):
    """HTTP 401 exception for expired JWT sessions."""

    def __init__(self, detail: str = 'Token has expired.') -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        )
