from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


class Database:
    def __init__(self, database_url: str) -> None:
        self._engine = create_async_engine(database_url, poolclass=NullPool)
        self._session_factory = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )

    @property
    def session_factory(self) -> sessionmaker:
        return self._session_factory
