from django.shortcuts import render
from .serializer import ToListSerializer
from .models import ToList
from rest_framework import mixins 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerList



class ToListView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    

    permission_classes = [IsAuthenticated ]

    
    queryset = ToList.objects.all()
    serializer_class = ToListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)  

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ToListViewDetails (mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):
    
    permission_classes = [IsAuthenticated , OwnerList]

    
    queryset = ToList.objects.all()
    serializer_class = ToListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        




