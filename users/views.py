from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from users.serializers import MyTokenObtainPairSerializer, UserSerializer
from users.models import MyUser

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)
        
    
class UserLogout(APIView):
    def post(self, request):
        response = Response({
            "message": "로그아웃 완료"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response

    
class UserDetailView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(MyUser, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user = get_object_or_404(MyUser, id=user_id)
        #user_ = self.id
        #print(request.user)
        #print(user_)
        #print(user)
        #if user == self.user:
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #else:
        #    return Response({"message":"유저가 달라요."}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):
        user = get_object_or_404(MyUser, id=user_id)
        user.delete()
        return Response("삭제되었습니다.", status=status.HTTP_200_OK)

