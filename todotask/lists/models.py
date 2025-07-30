from django.db import models
from user.models import CustomeUser


class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.DateField()
    user = models.ForeignKey(
        CustomeUser,
        related_name='todo_lists',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} (by {self.user.username})"
