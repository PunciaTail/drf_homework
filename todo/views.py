from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from todo.serializers import TodoSerialize
from user.models import Users
from todo.models import Todos

class TodoView(APIView):
    def get(self, request):
        todo = Todos.objects.all()
        return Response(todo)
    def post(self, request):
        serialize = TodoSerialize(data=request.data)
        if serialize.is_valid():
            # user를 저장하지 않으면 에러남
            serialize.validated_data['user'] = request.user
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':f'${serialize.errors}'}, status=status.HTTP_400_BAD_REQUEST)