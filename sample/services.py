from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from .dao import UserDAO, PermissionsDAO


class UserService:
    def __init__(
            self,
            user_dao: UserDAO,
            permissions_dao: PermissionsDAO,
            session: AsyncSession
    ) -> None:
        self._user_dao = user_dao
        self._permissions_dao = permissions_dao
        self._session = session

    async def get_users_list(self) -> None:
        await self._user_dao.list()

    async def get_user(self, user_id: int) -> None:
        await self._user_dao.get(user_id=user_id)
        await self._user_dao.create()
        await self._permissions_dao.list()
        await self._session.commit()
