from rest_framework import serializers
from backend.models.user import User

class UserCreateSerializer(serializers.Serializer):
    user_name = serializers.CharField(
        required=True,
        max_length=255
    )
    user_email_address = serializers.EmailField(
        required=True
    )
    user_mobile_number = serializers.CharField(
        required=True,
        max_length=255
    )

