from __future__ import annotations
from typing import Generator, TYPE_CHECKING
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from sqlalchemy.orm.session import sessionmaker

from .database import Database


def provide_db(db_url: str) -> Database:
    return Database(database_url=db_url)


async def provide_session_stub() -> None:
    ...


class ProvideSession:
    def __init__(self, session_factory: sessionmaker) -> None:
        self._session_factory = session_factory

    async def __call__(self) -> Generator[AsyncSession, None, None]:
        async with self._session_factory() as session:
            yield session
