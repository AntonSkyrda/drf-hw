from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from apps.pizza.filters import PizzaFilter
from apps.pizza.models import Pizza
from apps.pizza.serializers import PizzaPhotoSerializer, PizzaSerializer


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


class PizzaAddPhotoView(UpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaPhotoSerializer
    http_method_names = ["put"]

    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)
