from .serializer import ToDoListSerializer
from .models import ToDoList
from rest_framework import mixins, generics
from rest_framework.throttling import UserRateThrottle
from .mixins import ListPermissionMixins


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
        return ToDoList.objects.filter(user=self.request.user)

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
    ListPermissionMixins,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = ToDoListSerializer
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        title = self.request.data.get("title")
        return ToDoList.objects.filter(
            title=title,
            user=self.request.user
        ).order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
