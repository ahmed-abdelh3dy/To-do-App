from rest_framework import serializers 
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'status']
        read_only_fields = ['todo_list']


    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.method == 'PATCH':
            if set(attrs.keys()) - {'status'}:
                raise serializers.ValidationError("You can only update the status field.")
        return attrs    
