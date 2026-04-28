from django_filters import rest_framework

from apps.pizza.models import Pizza


class PizzaFilter(rest_framework.FilterSet):
    price_gt = rest_framework.NumberFilter(field_name="price", lookup_expr="gt")
    price_gte = rest_framework.NumberFilter(field_name="price", lookup_expr="gte")
    price_lt = rest_framework.NumberFilter(field_name="price", lookup_expr="lt")
    price_lte = rest_framework.NumberFilter(field_name="price", lookup_expr="lte")

    size_gt = rest_framework.NumberFilter(field_name="size", lookup_expr="gt")
    size_gte = rest_framework.NumberFilter(field_name="size", lookup_expr="gte")
    size_lt = rest_framework.NumberFilter(field_name="size", lookup_expr="lt")
    size_lte = rest_framework.NumberFilter(field_name="size", lookup_expr="lte")

    name_startswith = rest_framework.CharFilter(
        field_name="name", lookup_expr="istartswith"
    )
    name_endswith = rest_framework.CharFilter(
        field_name="name", lookup_expr="iendswith"
    )
    name_contains = rest_framework.CharFilter(
        field_name="name", lookup_expr="icontains"
    )

    class Meta:
        model = Pizza
        fields = []
