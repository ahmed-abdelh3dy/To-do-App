from rest_framework import serializers
from .models import CustomeUser
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ['id', 'username' , 'password' , 'email' ]
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def validate_username(self, value):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError("Username can only contain letters, numbers, and underscores.")
        if len(value) < 7:
            raise serializers.ValidationError("Username must be at least 7 characters.")
        return value
