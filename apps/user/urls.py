from django.conf.urls.static import static
from django.urls import path

from configs import settings

from apps.user.views import (
    UserIsActiveToggleAPIView,
    UserIsStaffToggleAPIView,
    UserListCreateView,
    UserRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("", UserListCreateView.as_view(), name="user_list_create"),
    path("<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view(), name="user_detail"),
    path(
        "<int:pk>/is-staff/", UserIsStaffToggleAPIView.as_view(), name="user_is_staff"
    ),
    path(
        "<int:pk>/is-active/",
        UserIsActiveToggleAPIView.as_view(),
        name="user_is_active",
    ),
]
