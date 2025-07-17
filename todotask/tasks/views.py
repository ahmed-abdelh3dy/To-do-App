from django.shortcuts import render , get_object_or_404
from .models import ToTasks
from .serializers import ToTaskSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework import generics
from lists.models import ToList



class ToTaskView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = ToTaskSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToTasks.objects.filter(list_id=self.kwargs.get('list_pk') , status = 'noncompleted')

    def perform_create(self, serializer):
            the_list= get_object_or_404(ToList ,id = self.kwargs.get('list_pk') , user_id = self.request.user.id )
            serializer.save(list_id=the_list)
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ToTaskDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    serializer_class = ToTaskSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self ):
        list_id = self.kwargs.get('list_pk')
        return ToTasks.objects.filter(list_id=list_id  )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class SearchTaskView(mixins.ListModelMixin,
                 generics.GenericAPIView):

    serializer_class = ToTaskSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToTasks.objects.filter(name=self.request.data.get('name') , list_id = self.kwargs.get('list_pk') )

    def get(self, request, *args, **kwargs ):
        return self.list(request, *args, **kwargs)


