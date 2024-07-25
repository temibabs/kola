import logging
import os

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from kola.db.base import DB, M

user = os.getenv("DB_USER", None)
password = os.getenv("DB_PASS", None)
host = os.getenv("DB_HOST", None)
name = os.getenv("DB_NAME", "babs")
port = os.getenv("DB_PORT", 5432)
engine = None

logger = logging.getLogger(__name__)


def create_engine():
    global engine

    if engine:
        return engine
    else:
        engine = create_async_engine(url=f"mysql+aiomysql://{user}:{password}@{host}:{port}/{name}")

    return engine


class MySQL(DB[M]):

    def __init__(self, cls: type[M]):
        super().__init__(cls)
        self.engine = create_engine()

    async def insert(self, obj: M) -> bool:
        async with AsyncSession(self.engine) as session:
            try:
                session.add(obj)
                await session.commit()
                await session.refresh(obj)
                return True
            except Exception as e:
                logger.error("Unable to insert record", e)
                return False

    async def select(self, criteria: dict, limit: int = 10, offset: int = 0) -> list[M]:
        async with AsyncSession(self.engine) as session:
            statement = select(self.cls)
            try:
                for k, v in criteria.items():
                    attribute = getattr(self.cls, k)
                    statement = statement.where(attribute == v)
            except AttributeError as a:
                logger.error(f"Attribute {k} does not exist in {self.cls}", a)
                raise a
            statement = statement.limit(limit=limit).offset(offset=offset)

            results = await session.execute(statement=statement)
            return results.scalars().all()

    async def update(self, obj: M, update: dict) -> bool:
        if not update:
            return obj

        async with AsyncSession(self.engine) as session:
            try:
                if obj.id is None:
                    raise ValueError("Object does not exist in database")
                for k, v in update.items():
                    setattr(obj, k, v)
                session.add(obj)
                await session.commit()
                await session.refresh(obj)
            except Exception as e:
                logger.error("Unable to update object", e)
                raise e
            else:
                return obj

    async def delete(self, obj: M) -> bool:
        async with AsyncSession(self.engine) as session:
            try:
                await session.delete(obj)
                await session.commit()
                return True
            except Exception as e:
                logger.error("Unable to delete record", e)
                return False
