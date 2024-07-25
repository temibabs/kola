from fastapi import FastAPI

from kola.router import product_router, invoice_router
from kola.seed import seed_db

app = FastAPI()

app.include_router(router=product_router, prefix="/api/products")
app.include_router(router=invoice_router, prefix="/api/invoices")


# @app.on_event("startup")
# async def seed():
#     await seed_db()
