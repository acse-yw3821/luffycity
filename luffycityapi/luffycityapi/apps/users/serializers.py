import re, constants
from rest_framework import serializers
from authenticate import MyTokenObtainPairSerializer
from .models import User
from tencentcloudapi import TencentCloudAPI, TencentCloudSDKException
from django_redis import get_redis_connection


class UserRegisterModelSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(required=True, write_only=True)
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True, help_text="短信验证码")
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
        redis = get_redis_connection("sms_code")
        code = redis.get(f"sms_{mobile}")
        if code is None:
            """获取不到验证码，则表示验证码已经过期了"""
            raise serializers.ValidationError("验证码失效或已过期！", code="sms_code")
        # 从redis提取的数据，字符串都是bytes类型，所以decode
        print(f"code={code.decode()}, sms_code={data.get('sms_code')}")

        if code.decode() != data.get("sms_code"):
            raise serializers.ValidationError(detail="短信验证码错误！", code="sms_code")
        # 删除掉redis中的短信，后续不管用户是否注册成功，至少当前这条短信验证码已经没有用处了
        redis.delete(f"sms_{mobile}")
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
