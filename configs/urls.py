from django.urls import include, path

urlpatterns = [
    path("pizzas/", include("apps.pizza.urls")),
]
