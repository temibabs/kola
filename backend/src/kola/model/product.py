from uuid import UUID, uuid4

from sqlmodel import Field

from kola.model.base import Model
from kola.util import get_image


class Product(Model, table=True):

    uuid: UUID = Field(default_factory=uuid4, index=True, nullable=False)
    name: str = Field(nullable=False)
    description: str
    price: float = Field(nullable=False)
    image_url: str = Field(default=get_image())
