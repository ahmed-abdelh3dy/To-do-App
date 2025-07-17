from rest_framework import permissions
from .permissions import OwnerList


class ListPermissionMixins():
    permission_classes = [permissions.IsAuthenticated , OwnerList]