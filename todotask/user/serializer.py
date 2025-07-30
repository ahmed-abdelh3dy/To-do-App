from rest_framework import serializers
from .models import CustomeUser
import re
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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


    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value
