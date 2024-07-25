import logging
import os
from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from kola.model.base import Model

M = TypeVar("M", bound=Model)

engine = None
user = os.getenv("DB_USER", None)
password = os.getenv("DB_PASS", None)
host = os.getenv("DB_HOST", None)
name = os.getenv("DB_NAME", "babs")
port = os.getenv("DB_PORT", 5432)

logger = logging.getLogger(__name__)


class DB(Generic[M], metaclass=ABCMeta):

    def __init__(self, cls: type[M]):
        self.cls = cls

    @abstractmethod
    async def insert(self, obj: M) -> bool:
        ...

    @abstractmethod
    async def select(self, criteria: dict) -> list[M]:
        ...

    @abstractmethod
    async def update(self, obj: M, update: dict) -> bool:
        ...

    @abstractmethod
    async def delete(self, obj: M) -> bool:
        ...
