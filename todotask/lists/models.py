from django.db import models
from user.models import CustomeUser


class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.DateField()
    user = models.ForeignKey(
        CustomeUser, related_name="todo_lists", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} (by {self.user.username})"


class ToDoListPermission(models.Model):
    PERMISSION_CHOICES = (
        ("read", "Read Only"),
        ("write", "Full Crud"),
    )

    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    todo_list = models.ForeignKey(
        ToDoList, on_delete=models.CASCADE, related_name="permissions"
    )
    permission_type = models.CharField(
        max_length=10, choices=PERMISSION_CHOICES, default="read"
    )

    class Meta:
        unique_together = ("user", "todo_list")
