from rest_framework import serializers
from users.models import MyUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'password', 'username', 'gender', 'age', 'introduction']

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        # user = super().update(instance, validated_data)
        # password = user.password
        # user.set_password(password)
        # user.save()
        # return user
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.introduction = validated_data.get('introduction', instance.introduction)

        instance.set_password(instance.password)
        instance.save()
        return instance
    # 이메일 수정 시도 시 이메일은 수정 못한다는 내용 리턴.. 받고싶음.
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['username'] = user.username
        token['gender'] = user.gender
        token['age'] = user.age

        return token