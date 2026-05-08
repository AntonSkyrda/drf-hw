from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("password",)
