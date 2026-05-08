from django.contrib.auth import get_user_model

from rest_framework.permissions import BasePermission

User = get_user_model()

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_staff and request.user.is_superuser
        )
