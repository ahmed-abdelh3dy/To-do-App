from django.shortcuts import render, get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics
from lists.models import ToDoList
from rest_framework.throttling import UserRateThrottle
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Tasks"])
class TaskListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return Task.objects.filter(todo_list=self.kwargs.get("list_pk"), status="noncompleted")

    def perform_create(self, serializer):
        task_list = get_object_or_404(ToDoList, id=self.kwargs.get("list_pk"), user_id=self.request.user.id)
        serializer.save(todo_list=task_list)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@extend_schema(tags=["Tasks"])
class TaskDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return Task.objects.filter(todo_list=self.kwargs.get("list_pk"))

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@extend_schema(tags=["Tasks"])
class TaskSearchView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return Task.objects.filter(name=self.request.data.get("name"), todo_list=self.kwargs.get("list_pk"))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
