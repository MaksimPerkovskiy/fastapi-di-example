from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class BaseDao:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
    

class UserDAO(BaseDao):
    async def create(self) -> None:
        print(self._session)
        ...
    
    async def list(self) -> None:
        print(self._session)
        ...
    
    async def get(self, user_id: int) -> None:
        print(self._session)
        ...


class PermissionsDAO(BaseDao):
    async def create(self) -> None:
        print(self._session)
        ...
    
    async def list(self) -> None:
        print(self._session)
        ...
    
    async def get(self, user_id: int) -> None:
        print(self._session)
        ...
