from typing import Dict, Type

from fastapi import status

from src.core.exceptions.api.users import (
    TokenExpiredAPIException,
    UnauthorizedAPIException,
    UserAPIException,
    UserConflictAPIException,
    UserNotFoundAPIException,
)
from src.core.exceptions.base import AppError
from src.core.exceptions.services.users import (
    InvalidCredentialsError,
    InvalidTokenError,
    RefreshTokenExpiredError,
    RefreshTokenNotFoundError,
    TokenExpiredError,
    UserAlreadyExistsError,
    UserNotFoundError,
)


class BaseExceptionsMapper:
    """Base mapper for registering service to API exception relations."""

    MAP: Dict[Type[AppError], Type[UserAPIException]] = {}

    @classmethod
    def convert(cls, exc: AppError) -> UserAPIException:
        """Find and return matching API exception for given service error."""
        for service_class, api_class in cls.MAP.items():
            if isinstance(exc, service_class):
                return api_class()
        return UserAPIException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )


class UsersExcMapper(BaseExceptionsMapper):
    """Exception mapper dedicated to user and authentication errors."""

    MAP = {
        UserAlreadyExistsError: UserConflictAPIException,
        UserNotFoundError: UserNotFoundAPIException,
        InvalidCredentialsError: UnauthorizedAPIException,
        # Token Validation Mappings
        RefreshTokenNotFoundError: UnauthorizedAPIException,
        InvalidTokenError: UnauthorizedAPIException,
        RefreshTokenExpiredError: TokenExpiredAPIException,
        TokenExpiredError: TokenExpiredAPIException,
    }


async def get_mapper(exc: AppError) -> BaseExceptionsMapper | None:
    """Factory to get the correct mapper based on the domain AppError."""
    if isinstance(exc, AppError):
        return UsersExcMapper()
    return None
