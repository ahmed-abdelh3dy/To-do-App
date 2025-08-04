from rest_framework import serializers
from .models import ToDoList , ToDoListPermission


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id' , 'title' , 'deadline']
        read_only_fields = ('user' , )



class InvitationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoListPermission
        fields = ['user' , 'permission_type' , 'todo_list']
        
        