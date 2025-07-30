from rest_framework.permissions import BasePermission

class OwnerTask(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.todo_list == request.user.useres.id
