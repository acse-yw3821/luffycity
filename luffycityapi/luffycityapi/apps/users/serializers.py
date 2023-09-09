import re, constants
from rest_framework import serializers
from authenticate import MyTokenObtainPairSerializer
from .models import User


class UserRegisterModelSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(required=True, write_only=True)
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["mobile", "password", "re_password", "sms_code", "token"]
        extra_kwargs = {
            "mobile": {
                "required": True, "write_only": True
            },
            "password": {
                "required": True, "write_only": True, "min_length": 6, "max_length": 16,
            },
        }

    def validate(self, data):
        # 手机号格式验证
        mobile = data.get("mobile", None)
        if not re.match("^1[3-9]\d{9}$", mobile):
            raise serializers.ValidationError(detail="手机号格式不正确！", code="mobile")

        password = data.get("password")
        re_password = data.get("re_password")
        if password != re_password:
            raise serializers.ValidationError(detail="两次密码不一致！", code="password")

        if User.objects.filter(mobile=mobile).first():
            raise serializers.ValidationError(detail="手机号已注册！")

        # TODO: 验证手机验证码


        return data

    def create(self, validated_data):
        """保存用户信息，完成注册"""
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")

        user = User.objects.create_user(
            username=mobile,
            mobile=mobile,
            password=password,
            avatar=constants.DEFAULT_USER_AVATAR,
        )
        # 注册成功以后，免登陆
        user.token = MyTokenObtainPairSerializer.get_token(user)
        return user


