from django.conf.urls.static import static
from django.urls import include, path

from configs import settings

urlpatterns = [
    path("pizzas/", include("apps.pizza.urls"), name="pizzas"),
    path("auth/", include("apps.auth.urls"), name="auth"),
    path("users/", include("apps.user.urls"), name="users"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)