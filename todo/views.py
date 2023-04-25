from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from todo.serializers import TodoSerialize, TodoCreateSerialize
from user.models import Users
from todo.models import Todos

class TodoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        todo = Todos.objects.all()
        serialize = TodoSerialize(todo, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serialize = TodoCreateSerialize(data=request.data)
        if serialize.is_valid():
            # user를 저장하지 않으면 에러남
            serialize.validated_data['user'] = request.user
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serialize.errors}'}, status=status.HTTP_400_BAD_REQUEST)
        
class TodoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todo_id):
        todo = get_object_or_404(Todos, id=todo_id)
        if request.user == todo.user:
            serialize = TodoSerialize(todo)
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, todo_id):
        todo = get_object_or_404(Todos, id=todo_id)
        if request.user == todo.user:
            serialize = TodoCreateSerialize(todo, data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data, status=status.HTTP_200_OK)
            else:
                return Response({'message':'데이터가 옳바르지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)   
    
    def delete(self, request, todo_id):
        todo = get_object_or_404(Todos, id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return Response({'message':'삭제 완료'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message':'권한이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST) 