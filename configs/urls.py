from django.urls import include, path

urlpatterns = [
    path("pizzas/", include("apps.pizza.urls"), name="pizzas"),
    path("auth/", include("apps.auth.urls"), name="auth"),
    path("users/", include("apps.user.urls"), name="users"),
]
