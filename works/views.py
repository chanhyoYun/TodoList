from rest_framework.response import Response
from rest_framework.views import APIView
from works.serializers import ToDoSerializer
from rest_framework import status
from works.models import ToDoList
from rest_framework.generics import get_object_or_404
from users.models import MyUser


class ToDoListView(APIView):
    def post(self, request):
        user = get_object_or_404(MyUser, pk=request.user.id)
        print(user)
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save(commit=False)
            #serializer.author = user
            serializer.save()
            return Response({"message":"할일 저장"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        works = ToDoList.objects.all()
        serializer = ToDoSerializer(works, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ToDoListDetailView(APIView):
    def put(self, request, work_id):
        work = get_object_or_404(ToDoList, pk=work_id)
        serializer = ToDoSerializer(work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, work_id):
        work = get_object_or_404(ToDoList, pk=work_id)
        work.delete()
        return Response({"message":"삭제완료"}, status=status.HTTP_200_OK)