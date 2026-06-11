from src.core.exceptions.services.users import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from src.schemas.users import SUser, SUserRegister
from src.services.auth.security import security
from src.services.base import BaseService


class UsersService(BaseService):
    """
    Service layer for User entities and profile management.
    """

    async def register_user(self, user_data: SUserRegister) -> SUser:
        """
        Register a new user and return validated user data.
        """
        existing = await self.db.users.get_user_by_username(user_data.username)
        if existing:
            raise UserAlreadyExistsError()

        user_orm = await self.db.users.create_user(
            username=user_data.username,
            password_hash=security.hash_password(user_data.password),
        )
        await self.db.commit()

        return SUser.model_validate(user_orm)

    async def get_user_profile(self, attr_value: int | str) -> SUser:
        """
        Retrieve a user profile by its ID or username.
        """
        if isinstance(attr_value, int):
            user_orm = await self.db.users.get_user_by_id(attr_value)
        else:
            user_orm = await self.db.users.get_user_by_username(
                str(attr_value)
            )

        if not user_orm:
            raise UserNotFoundError()

        return SUser.model_validate(user_orm)

    async def delete_account(self, user_id: int) -> None:
        """
        Remove a user and all associated data from the database.
        """
        user_orm = await self.db.users.get_user_by_id(user_id)
        if not user_orm:
            raise UserNotFoundError()
        await self.db.users.delete(db_obj=user_orm)
        await self.db.commit()
