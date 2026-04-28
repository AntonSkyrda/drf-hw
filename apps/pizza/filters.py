from django_filters import rest_framework as filters

from apps.pizza.models import Pizza


class PizzaFilter(filters.FilterSet):
    price_gt = filters.NumberFilter(field_name="price", lookup_expr="gt")
    price_gte = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_lt = filters.NumberFilter(field_name="price", lookup_expr="lt")
    price_lte = filters.NumberFilter(field_name="price", lookup_expr="lte")

    size_gt = filters.NumberFilter(field_name="size", lookup_expr="gt")
    size_gte = filters.NumberFilter(field_name="size", lookup_expr="gte")
    size_lt = filters.NumberFilter(field_name="size", lookup_expr="lt")
    size_lte = filters.NumberFilter(field_name="size", lookup_expr="lte")

    name_startswith = filters.CharFilter(
        field_name="name", lookup_expr="istartswith"
    )
    name_endswith = filters.CharFilter(
        field_name="name", lookup_expr="iendswith"
    )
    name_contains = filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )

    class Meta:
        model = Pizza
        fields = []
