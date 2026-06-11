from src.models.users import UsersOrm
from src.repositories.base import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    """
    Repository for managing User entity database operations.
    """

    model = UsersOrm

    async def create_user(self, username: str, password_hash: str) -> UsersOrm:
        """
        Creates a new user record in the database.

        Args:
            username: The username of the new user.
            password_hash: The hashed password of the new user.

        Returns:
            UsersOrm: The created user database object.
        """
        user = self.model(username=username, password_hash=password_hash)
        self.session.add(user)
        await self.session.flush()
        return user

    async def get_user_by_id(self, user_id: int) -> UsersOrm | None:
        """
        Retrieves a user by their unique ID.

        Args:
            user_id: The integer ID of the user to retrieve.

        Returns:
            UsersOrm | None: The user object if found, otherwise None.
        """
        return await self.get_one_by_field(attr_name='id', attr_value=user_id)

    async def get_user_by_username(self, username: str) -> UsersOrm | None:
        """
        Retrieves a user by their username.

        Args:
            username: The string username of the user to retrieve.

        Returns:
            UsersOrm | None: The user object if found, otherwise None.
        """
        return await self.get_one_by_field(
            attr_name='username', attr_value=username
        )
