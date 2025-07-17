from .serializer import ToListSerializer
from .models import ToList
from rest_framework import mixins
from rest_framework import generics
from rest_framework.throttling import UserRateThrottle
from .mixins import ListPermissionMixins


class ToListView(
    ListPermissionMixins,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    queryset = ToList.objects.all()
    serializer_class = ToListSerializer
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return ToList.objects.filter(user_id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ToListViewDetails(
    ListPermissionMixins,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):

    queryset = ToList.objects.all()
    serializer_class = ToListSerializer
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SearchListView(
    ListPermissionMixins, mixins.ListModelMixin, generics.GenericAPIView
):

    serializer_class = ToListSerializer
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return ToList.objects.filter(
            title=self.request.data.get("title"), user_id=self.request.user.id
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
