from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics
from lists.models import ToDoList
from rest_framework.throttling import UserRateThrottle
from drf_spectacular.utils import extend_schema
from .CustomResponse import CustomResponseMixin
from lists.permissions import HasTaskPermission
from rest_framework.exceptions import PermissionDenied
from lists.models import ToDoListPermission


@extend_schema(tags=["Tasks"])
class TaskListCreateView(
    CustomResponseMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return Task.objects.filter(
            todo_list=self.kwargs.get("list_pk"), status="noncompleted"
        )

    def perform_create(self, serializer):
        todo_list = get_object_or_404(ToDoList, id=self.kwargs.get("list_pk"))

        try:
            permission = ToDoListPermission.objects.get(
                user=self.request.user, todo_list=todo_list
            )
            # print (permission.permission_type)

        except ToDoListPermission.DoesNotExist:
            raise PermissionDenied("You do not have permission.")

        if permission.permission_type != "write":
            raise PermissionDenied("You only have read access to this list.")

        serializer.save(todo_list=todo_list)

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        return self.custom_response(
            response.data, "Task list fetched", response.status_code
        )

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return self.custom_response(response.data, "Task created", response.status_code)


@extend_schema(tags=["Tasks"])
class TaskDetailView(
    CustomResponseMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, HasTaskPermission]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return Task.objects.filter(todo_list=self.kwargs.get("list_pk"))

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        return self.custom_response(response.data, "Task details", response.status_code)

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return self.custom_response(response.data, "Task updated", response.status_code)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return self.custom_response(
            response.data, "Task status updated", response.status_code
        )

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return self.custom_response(None, "Task deleted", response.status_code)


@extend_schema(tags=["Tasks"])
class TaskSearchView(
    CustomResponseMixin, mixins.ListModelMixin, generics.GenericAPIView
):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        name = self.request.query_params.get("name")
        return Task.objects.filter(
            name__icontains=name, todo_list=self.kwargs.get("list_pk")
        )

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        return self.custom_response(
            response.data, "Search results", response.status_code
        )
