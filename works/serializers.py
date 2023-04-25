from rest_framework import serializers
from works.models import ToDoList
from users.models import MyUser


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoList
        fields = ["id", "title", "is_complete", "created_at", "updated_at", "completion_at"]