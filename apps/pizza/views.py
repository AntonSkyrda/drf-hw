from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from apps.pizza.filters import PizzaFilter
from apps.pizza.models import Pizza
from apps.pizza.serializers import PizzaSerializer


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
