import os
from uuid import uuid4


def upload_pizza_photo(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    folder = instance.name or "pizzas"

    return os.path.join(folder, f"{uuid4()}.{ext}")
