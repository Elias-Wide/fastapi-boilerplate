from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
    status,
)

from src.config import settings
from src.dependencies.db_manager import DBManagerDep
from src.dependencies.users import get_current_user
from src.models.users import UsersOrm
from src.schemas.tokens import SLoginRequest, SRefreshRequest, STokenPair
from src.schemas.users import SUser, SUserRegister
from src.services.auth.auth import AuthServiceJWT
from src.services.auth.tokens import BaseCookie, get_cookie_config
from src.services.users import UsersService

router = APIRouter(prefix='/users', tags=['users'])


def _set_token_cookies(
    response: Response, access_token: str, refresh_token: str
) -> None:
    """Set access and refresh tokens in HTTP-only cookies."""
    cookie: BaseCookie = get_cookie_config()
    response.set_cookie(
        **cookie.get_set_params(
            key=settings.auth.access_cookie_name,
            value=access_token,
            max_age_minutes=settings.auth.access_token_expires_minutes,
        )
    )
    response.set_cookie(
        **cookie.get_set_params(
            key=settings.auth.refresh_cookie_name,
            value=refresh_token,
            max_age_minutes=settings.auth.refresh_token_expires_minutes,
        )
    )


def _delete_token_cookies(response: Response) -> None:
    """Clear access and refresh tokens from cookies."""
    cookie: BaseCookie = get_cookie_config()
    response.delete_cookie(
        **cookie.get_delete_params(key=settings.auth.access_cookie_name)
    )
    response.delete_cookie(
        **cookie.get_delete_params(key=settings.auth.refresh_cookie_name)
    )


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: SUserRegister,
    db: DBManagerDep,
) -> SUser:
    """Register a new user and return the user data."""
    service = UsersService(db)
    return await service.register_user(user_data)


@router.post('/login', summary='Authenticate user and obtain JWT tokens')
async def login(
    data: SLoginRequest,
    db: DBManagerDep,
    response: Response,
) -> STokenPair:
    """Authenticate user and set JWT tokens in cookies."""
    jwt_service = AuthServiceJWT(db)
    access_token, refresh_token = await jwt_service.login(
        data.username, data.password
    )
    _set_token_cookies(response, access_token, refresh_token)
    return STokenPair(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post(
    '/logout',
    summary='Log out the current user',
)
async def logout_user(
    user: Annotated[UsersOrm, Depends(get_current_user)],
    db: DBManagerDep,
    response: Response,
    request: Request,
):
    refresh_token = request.cookies.get('refresh_token')
    auth_service = AuthServiceJWT(db)
    if refresh_token:
        await auth_service.delete_refresh_token(refresh_token)
    _delete_token_cookies(response)
    return {'detail': 'Successfully logged out'}


@router.post(
    '/token/refresh', summary='Refresh JWT tokens using a refresh token'
)
async def refresh_tokens(
    data: SRefreshRequest, response: Response, db: DBManagerDep
) -> STokenPair:
    """Refresh session tokens and update cookies using a refresh token."""
    jwt_service = AuthServiceJWT(db)
    pair = await jwt_service.refresh(data.refresh_token)
    _set_token_cookies(response, pair.access_token, pair.refresh_token)
    return pair


@router.get('/me')
async def get_profile(
    user: Annotated[UsersOrm, Depends(get_current_user)],
    db: DBManagerDep,
) -> SUser:
    service = UsersService(db)
    return await service.get_user_profile(user.id)
