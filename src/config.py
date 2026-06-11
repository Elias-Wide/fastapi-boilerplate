from pathlib import Path
from typing import Optional

from pydantic import Field, SecretStr, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.constants.core import DEFAULT_JWT_ALGORITHM

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / '.env'


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH, env_file_encoding='utf-8', extra='ignore'
    )


class DatabaseConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix='db_')

    host: str
    name: str
    password: SecretStr
    port: int
    user: str
    url: Optional[str] = Field(default=None)

    test_host: str = 'localhost'
    test_name: str = 'test_db'
    test_password: SecretStr = SecretStr('postgres')
    test_port: int = 5432
    test_user: str = 'postgres'
    test_url: Optional[str] = Field(default=None)

    @staticmethod
    def create_url(info: ValidationInfo, prefix: str = '') -> str:
        """Build connection string from validation info using a prefix."""
        data = info.data
        user = data.get(f'{prefix}user')
        pwd = data.get(f'{prefix}password')
        host = data.get(f'{prefix}host')
        port = data.get(f'{prefix}port')
        name = data.get(f'{prefix}name')

        secret = pwd.get_secret_value() if pwd else ''
        return f'postgresql+asyncpg://{user}:{secret}@{host}:{port}/{name}'

    @field_validator('url', mode='before')
    @classmethod
    def assemble_url(cls, v: Optional[str], info: ValidationInfo) -> str:
        """Assemble main database URL if not provided."""
        return v if v else cls.create_url(info, prefix='')

    @field_validator('test_url', mode='before')
    @classmethod
    def assemble_test_url(cls, v: Optional[str], info: ValidationInfo) -> str:
        """Assemble test database URL if not provided."""
        return v if v else cls.create_url(info, prefix='test_')


class UserAuthConfig(ConfigBase):
    """
    User authentication settings, including JWT configuration.
    """

    jwt_algorithm: str = Field(
        default=DEFAULT_JWT_ALGORITHM, alias='AUTH_JWT_ALGORITHM'
    )
    jwt_secret_key: str = Field(alias='AUTH_JWT_SECRET_KEY')
    access_token_expires_minutes: int = Field(
        default=15,
        alias='AUTH_ACCESS_TOKEN_EXPIRES_MINUTES',
    )
    refresh_token_expires_minutes: int = Field(
        default=60 * 24 * 30,
        alias='AUTH_REFRESH_TOKEN_EXPIRES_MINUTES',
    )
    session_ttl_minutes: int = Field(
        default=60 * 24,
        alias='AUTH_SESSION_TTL_MINUTES',
    )
    session_extend_minutes: int = Field(
        default=60 * 24 * 7,
        alias='AUTH_SESSION_EXTEND_MINUTES',
    )
    session_rolling_interval_minutes: int = Field(
        default=10,
        alias='AUTH_SESSION_ROLLING_INTERVAL_MINUTES',
    )
    session_absolute_timeout_days: int = Field(
        default=30,
        alias='AUTH_SESSION_ABSOLUTE_TIMEOUT_DAYS',
    )
    session_cookie_name: str = Field(
        default='session_id',
        alias='AUTH_SESSION_COOKIE_NAME',
    )
    session_cookie_secure: bool = Field(
        default=False,
        alias='AUTH_SESSION_COOKIE_SECURE',
    )
    session_cookie_domain: str | None = Field(
        default=None,
        alias='AUTH_SESSION_COOKIE_DOMAIN',
    )
    access_cookie_name: str = Field(
        default='access_token',
        alias='AUTH_ACCESS_COOKIE_NAME',
    )
    refresh_cookie_name: str = Field(
        default='refresh_token',
        alias='AUTH_REFRESH_COOKIE_NAME',
    )

    model_config = SettingsConfigDict(env_prefix='auth_')


class AppConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix='app_')
    name: str = 'fastapi-app'
    mode: str = 'dev'


class Settings(BaseSettings):
    app: AppConfig = Field(default_factory=AppConfig)
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    auth: UserAuthConfig = Field(default_factory=UserAuthConfig)

    @classmethod
    def load(cls) -> 'Settings':
        return cls()


settings: Settings = Settings.load()
