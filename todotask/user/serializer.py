from rest_framework import serializers
from .models import CustomeUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ['id', 'username' , 'password' , 'email' ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
