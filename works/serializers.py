from rest_framework import serializers
from works.models import ToDoList
from users.models import MyUser

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["id", "email", "username"]

class ToDoSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = ToDoList
        fields = ["id", "title", "is_complete", "created_at", "updated_at", "completion_at", "author"]