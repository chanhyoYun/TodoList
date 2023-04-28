from rest_framework.response import Response
from rest_framework.views import APIView
from works.serializers import ToDoSerializer
from rest_framework import status
from works.models import ToDoList
from rest_framework.generics import get_object_or_404
from users.models import MyUser
from datetime import datetime


class ToDoListView(APIView):
    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":"할일 저장"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        works = ToDoList.objects.filter(user=request.user.id)
        serializer = ToDoSerializer(works, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ToDoListDetailView(APIView):
    def put(self, request, work_id): 
        work = get_object_or_404(ToDoList, pk=work_id)
        if work.user == request.user:
            serializer = ToDoSerializer(work, data=request.data)
            
            if serializer.is_valid():
                if serializer.validated_data.get("is_complete") == True:
                    work.completion_at = datetime.now().date()
                    serializer.save()
                else:
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({"message":"유저가 달라요."}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, work_id):
        work = get_object_or_404(ToDoList, pk=work_id)
        if work.user == request.user:
            work.delete()
            return Response({"message":"삭제완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"유저가 달라요."}, status=status.HTTP_400_BAD_REQUEST)