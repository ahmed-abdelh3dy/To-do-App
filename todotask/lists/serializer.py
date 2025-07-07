from rest_framework import serializers
from .models import ToList


class ToListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToList
        fields = ['id' , 'title' , 'deadline']
        read_only_fields = ('user_id' , )