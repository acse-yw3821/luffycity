# from rest_framework.generics import ListAPIView
from views import CacheListAPIView
from .serializers import NavModelSerializer, BannerModelSerializer
from .models import Nav, Banner
import constants
# 对日志调用
import logging

logger = logging.getLogger("django")


class NavHeaderListAPIView(CacheListAPIView):
    """顶部导航视图"""

    queryset = Nav.objects.filter(
        position=constants.NAV_HEADER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[
               :constants.NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(CacheListAPIView):
    """脚部导航视图"""
    queryset = Nav.objects.filter(
        position=constants.NAV_FOOTER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[
               :constants.NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer


class BannerListAPIView(CacheListAPIView):
    """轮播广告视图"""
    queryset = Banner.objects.filter(is_deleted=False, is_show=True).order_by("orders", "-id")[:constants.BANNER_SIZE]
    serializer_class = BannerModelSerializer
