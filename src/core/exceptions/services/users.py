from src.core.exceptions.base import AppError


class ServiceError(AppError):
    """Base exception for all service layer business logic."""

    msg = 'Business logic error occurred.'


class UserAlreadyExistsError(ServiceError):
    """Raised when registering a username or email that is already taken."""

    message: str = 'A user with these credentials already exists.'


class UserNotFoundError(ServiceError):
    """Raised when a user cannot be found in the database."""

    message: str = 'User not found.'


class InvalidCredentialsError(ServiceError):
    """Raised during login if password or username mismatch."""

    message: str = 'Invalid username or password.'


class RefreshTokenNotFoundError(ServiceError):
    """Raised when the provided refresh token is missing from the database."""

    message: str = 'Session not found or invalid.'


class RefreshTokenExpiredError(ServiceError):
    """Raised when the refresh token expiration time has passed."""

    message: str = 'Session has expired. Please log in again.'


class InvalidTokenError(ServiceError):
    """Raised when a JWT access token is malformed, invalid, or tampered with."""

    message: str = 'Invalid authentication token.'


class TokenExpiredError(ServiceError):
    """Raised when a JWT access token has expired."""

    message: str = 'Authentication token has expired.'
