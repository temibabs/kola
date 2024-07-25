import os
from random import randint

import requests
import shutil

category = "food"
IMG_URL = f"https://api.api-ninjas.com/v1/randomimage?category={category}"
IMG_API_KEY = os.getenv("IMG_API_KEY")


def get_image():
    id1 = randint(0, 300)
    id2 = randint(0, 300)
    return f"https://picsum.photos/seed/picsum/{id1}/{id2}"


def generate_invoice_number():
    return randint(1001, 9999)
