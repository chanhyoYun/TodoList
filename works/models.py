from django.db import models
from users.models import MyUser

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=50, blank=False)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateField(auto_now=True)
    author = models.ForeignKey(MyUser, null=True, on_delete=models.CASCADE, related_name="work_user")

    def __str__(self):
        return str(self.title)