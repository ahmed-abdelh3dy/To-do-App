from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
    username = models.CharField(max_length=50  , unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.email
    

