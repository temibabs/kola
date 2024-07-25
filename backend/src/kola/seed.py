from random import choice, random, randint

from kola.db.sql import MySQL
from kola.model import Product, Invoice, InvoiceItem

product_db: MySQL[Product] = MySQL(cls=Product)
invoice_db: MySQL[Invoice] = MySQL(cls=Invoice)
invoice_item_db: MySQL[InvoiceItem] = MySQL(cls=InvoiceItem)


async def seed_db():

    product_count = 30
    colors = ["Blue", "Yellow", "Green", "Black", "Blue"]
    for i in range(product_count):
        price = float(f"{random():.2f}") + randint(10, 20)
        color = choice(colors)
        product = Product(name=f"{color} Dress", description=f"A beautiful {color} dress", price=price)
        await product_db.insert(product)

    invoice_count = 10
    for i in range(invoice_count):
        customer_id = randint(1, 200)
        supplier_id = randint(1, 20)
        invoice = Invoice(
            customer_info=f"Customer #{customer_id}",
            supplier_info=f"Supplier #{supplier_id}",
        )
        await invoice_db.insert(invoice)

    for i in range(20):
        quantity = randint(1, 3)
        invoice_id = randint(1, invoice_count)
        product_id = randint(1, product_count)
        invoice_item = InvoiceItem(quantity=quantity, invoice_id=invoice_id, product_id=product_id)
        await invoice_item_db.insert(invoice_item)
