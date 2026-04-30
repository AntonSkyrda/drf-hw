from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.user.models import UserProfile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "first_name",
            "last_name",
            "age",
            "created_at",
            "updated_at",
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "profile",
        )
        read_only_fields = (
            "id",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        profile = validated_data.pop("profile")
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile)
        return user


class UserIsStaffUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("is_staff",)


class UserIsActiveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("is_active",)
