from .serializer import ToDoListSerializer, InvitationListSerializer
from .models import ToDoList
from rest_framework import mixins, generics
from rest_framework.throttling import UserRateThrottle
from .mixins import ListPermissionMixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDoList, ToDoListPermission
from user.models import CustomeUser
from django.shortcuts import get_object_or_404


class ToDoListView(
    ListPermissionMixins,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        owned = ToDoList.objects.filter(user=self.request.user)
        shared = ToDoList.objects.filter(permissions__user=self.request.user)

        return (owned | shared).distinct()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ToDoListDetailView(
    ListPermissionMixins,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ToDoListSearchView(
    ListPermissionMixins, mixins.ListModelMixin, generics.GenericAPIView
):
    serializer_class = ToDoListSerializer
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        title = self.request.data.get("title")
        return ToDoList.objects.filter(title=title, user=self.request.user).order_by(
            "id"
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class InviteUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = InvitationListSerializer

    def post(self, request, *args, **kwargs):
        list_id = request.data.get("list_id")
        username = request.data.get("username")
        permission_type = request.data.get("permission_type") or "read"

        todo_list = get_object_or_404(ToDoList, id=list_id)

        if todo_list.user != request.user:
            return Response({"error": "You are not the owner."}, status=403)

        invited_user = get_object_or_404(CustomeUser, username=username)

        if permission_type not in ["read", "write"]:
            return Response({"error": "permissions type wrong."}, status=403)

        ToDoListPermission.objects.update_or_create(
            user=invited_user,
            todo_list=todo_list,
            defaults={"permission_type": permission_type},
        )

        return Response({"message": "User invited successfully."})
