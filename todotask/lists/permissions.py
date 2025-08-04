from rest_framework.permissions import BasePermission , SAFE_METHODS
from .models import ToDoListPermission


# class OwnerList(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user



class HasToDoListPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True 

        try:
            permission = ToDoListPermission.objects.get(user=request.user, todo_list=obj)
        except ToDoListPermission.DoesNotExist:
            return False

        if request.method in SAFE_METHODS and permission.permission_type in ['read', 'write']:
            return True
        elif request.method not in SAFE_METHODS and permission.permission_type == 'write':
            return True

        return False



class HasTaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        todo_list = obj.todo_list

        try:
            permission = ToDoListPermission.objects.get(
                user=request.user,
                todo_list=todo_list
            )
        except ToDoListPermission.DoesNotExist:
            return False

        if request.method in SAFE_METHODS:
            return True

        return permission.permission_type == 'write'
