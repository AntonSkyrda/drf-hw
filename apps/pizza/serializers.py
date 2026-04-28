from rest_framework import serializers

from apps.pizza.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ("id", "name", "price", "size", "created_at", "updated_at")
