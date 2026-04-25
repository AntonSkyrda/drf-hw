from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    RetrieveUpdateAPIView,
    ListCreateAPIView,
)

from pizza.filters import PizzaFilter
from pizza.models import Pizza
from pizza.serializers import PizzaSerializer


class PizzaListCreateView(ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PizzaFilter

    ordering_fields = ["id", "name", "size", "price", "created_at", "updated_at"]
    ordering = ["id"]


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
