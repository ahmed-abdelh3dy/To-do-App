from rest_framework import serializers 
from .models import ToTasks

class ToTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToTasks
        fields = ['id' , 'name' , 'status'   ]
        read_only_fields = ('list_id' , )

