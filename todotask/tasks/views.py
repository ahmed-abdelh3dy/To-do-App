from django.shortcuts import render , get_object_or_404
from rest_framework import viewsets
from .models import ToTasks
from .serializers import ToTaskSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response



class ToTaskView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated ]
    queryset = ToTasks.objects.filter(status = 'noncompleted')
    serializer_class = ToTaskSerializers

    def perform_create(self, serializer):
        list_id =  self.request.user.lists.get(id = self.request.data.get('list_id'))
        serializer.save(list_id=list_id)  


    @action(detail=True, methods=['PATCH'])
    def complete(self , request , pk ):

        task = get_object_or_404(ToTasks , id = pk )
        serializer =  ToTaskSerializers( task , data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'task updated ': serializer.data} , status=201)
        return Response({'error': serializer.errors} , status=400)
