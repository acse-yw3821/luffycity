from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q


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


def get_user_by_account(account):
    """
    根据帐号信息获取user模型实例对象
    :param account: 账号信息，可以是用户名，也可以是手机号，甚至其他的可用于识别用户身份的字段信息
    :return: User对象 或者 None
    """
    return UserModel.objects.filter(Q(mobile=account) | Q(username=account) | Q(email=account)).first()


class CustomAuthBackend(ModelBackend):
    """
    自定义用户认证类[实现多条件登录]
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        多条件认证方法
           :param request: 本次客户端的http请求对象
           :param username:  本次客户端提交的用户信息，可以是user，也可以mobile或其他唯一字段
           :param password: 本次客户端提交的用户密码
           :param kwargs: 额外参数
           :return:
        """
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
            # 根据用户名信息useranme获取账户信息
        user = get_user_by_account(username)
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
