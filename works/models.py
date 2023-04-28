from django.db import models
from users.models import MyUser

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, blank=False)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateField(blank=True)

    def __str__(self):
        return str(self.title)