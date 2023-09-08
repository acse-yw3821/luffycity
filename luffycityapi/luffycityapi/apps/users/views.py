from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework import status


class MobileAPIView(APIView):
    def get(self, request, mobile):
        if User.objects.filter(mobile=mobile).first():
            return Response({"errmsg": "当前手机号已注册"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 如果查不到该手机号的注册记录，则证明手机号可以注册使用
            return Response({"errmsg": "OK"}, status=status.HTTP_200_OK)
