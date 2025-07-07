from django.db import models
from lists.models import ToList


class ToTasks(models.Model):
    TaskStatus = [
        ('completed', 'Completed'),
        ('noncompleted', 'Non Completed'),
    ]
    
    name = models.CharField(max_length=100)
    list_id = models.ForeignKey(ToList , related_name='tasks' , on_delete=models.CASCADE)
    status = models.CharField(max_length=50 , choices=TaskStatus )
