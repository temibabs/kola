from uuid import UUID, uuid4

from sqlmodel import Field

from kola.model.base import Model
from kola.util import generate_invoice_number


class Invoice(Model, table=True):

    uuid: UUID = Field(default_factory=uuid4, index=True, nullable=False)
    invoice_number: int = Field(default_factory=generate_invoice_number)
    customer_info: str
    supplier_info: str


class InvoiceItem(Model, table=True):

    __tablename__ = "invoice_item"

    invoice_id: int = Field(default=None, foreign_key="invoice.id")
    product_id: int = Field(default=None, foreign_key="product.id")
    quantity: int
