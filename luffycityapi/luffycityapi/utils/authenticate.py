from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        """
        自定义载荷信息
        :params user  用户模型实例对象
        """
        token = super().get_token(user)

        # Add custom claims
        if hasattr(user, "avatar"):
            token["avatar"] = user.avatar.url if user.avatar else ""
        if hasattr(user, "nickname"):
            token["nickname"] = user.nickname
        if hasattr(user, "money"):
            token["money"] = float(user.money)
        if hasattr(user, "credit"):
            token["credit"] = user.credit

        return token
