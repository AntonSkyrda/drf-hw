from django.urls import path, include

urlpatterns = [
    path("pizzas/", include("pizza.urls")),
]
