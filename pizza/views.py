from rest_framework.generics import (
    RetrieveUpdateAPIView,
    ListCreateAPIView,
)

from pizza.models import Pizza
from pizza.serializers import PizzaSerializer


class PizzaListCreateView(ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
