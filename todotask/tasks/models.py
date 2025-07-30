from django.db import models
from lists.models import ToDoList


class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ("completed", "Completed"),
        ("noncompleted", "Not Completed"),
    ]

    name = models.CharField(max_length=100)
    todo_list = models.ForeignKey(
        ToDoList, related_name="tasks", on_delete=models.CASCADE
    )
    status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.status}"
