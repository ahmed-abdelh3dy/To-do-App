from rest_framework import permissions
from .permissions import  HasToDoListPermission


class ListPermissionMixins():
    permission_classes = [permissions.IsAuthenticated , HasToDoListPermission]  