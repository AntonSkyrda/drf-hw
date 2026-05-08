from django.db import models

from core.models import BaseModel
from core.services.file_service import upload_pizza_photo


class Pizza(BaseModel):
    class Meta:
        db_table = "pizzas"

    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    price = models.FloatField()

    photo = models.ImageField(
        upload_to=upload_pizza_photo,
        blank=True,
    )


    def __str__(self):
        return self.name
