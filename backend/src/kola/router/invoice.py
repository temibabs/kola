import logging
from uuid import UUID

from fastapi import APIRouter, HTTPException

from kola.db import MySQL
from kola.model.invoice import Invoice

router = APIRouter()
logger = logging.getLogger(__name__)
invoice_db: MySQL[Invoice] = MySQL(cls=Invoice)


@router.get("/")
async def get_invoices():
    try:
        products = await invoice_db.select({}, limit=10, offset=0)
        return products
    except Exception as e:
        logger.error("Unable to get products", e)
        return HTTPException(status_code=500, detail="Something Happened!")


@router.get("/{id}")
async def get_product(id: UUID):
    try:
        product = await invoice_db.select({"uuid": id})
        return product
    except Exception as e:
        logger.error(f"Unable to get product with id: {id}", e)
        return HTTPException(status_code=500, detail="Something Happened!")
