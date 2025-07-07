from django.db import models
from user.models import CustomeUser



class ToList(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.DateField()
    user_id = models.ForeignKey(CustomeUser, related_name='lists' , on_delete=models.CASCADE)



    def __str__(self):
        return self.title
    