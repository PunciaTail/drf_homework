from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from user.serializers import UserSerialize
from user.models import Users


class UserView(APIView):
    def post(self, request):
        serialize = UserSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'message': '가입완료'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': f'${serialize.errors}'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserDetailView(APIView):
    def delete(self, request, user_id):
        compare_user = get_object_or_404(Users, id=user_id)
        if request.user == compare_user:
            compare_user.delete()
            return Response('회원 탈퇴.', status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('삭제 못함', status=status.HTTP_403_FORBIDDEN)
        
    def put(self, request, user_id):
        compare_user = get_object_or_404(Users, id=user_id)
        if request.user == compare_user:
            serialize = UserSerialize(compare_user, data=request.data)
            if serialize.is_valid():
                serialize.email=request.user.email,
                serialize.save()
            return Response('회원 수정', status=status.HTTP_200_OK)
        else:
            return Response('수정 못함', status=status.HTTP_403_FORBIDDEN)
        

