from django.db import models

from core.models import BaseModel


class Pizza(BaseModel):
    class Meta:
        db_table = "pizzas"

    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
