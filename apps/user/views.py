from django.contrib.auth import get_user_model

from rest_framework import serializers, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import UserSerializer

User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserIsStaffToggleAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)

        if user == request.user:
            raise serializers.ValidationError(
                "You can not change the status of your account."
            )

        user.is_staff = not user.is_staff
        user.save(update_fields=["is_staff"])

        return Response(
            {"id": user.id, "is_staff": user.is_staff},
            status=status.HTTP_200_OK,
        )


class UserIsActiveToggleAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)

        if user == request.user:
            raise serializers.ValidationError(
                "You can not change the status of your account."
            )

        user.is_active = not user.is_active
        user.save(update_fields=["is_active"])

        return Response(
            {"id": user.id, "is_active": user.is_active},
            status=status.HTTP_200_OK,
        )
