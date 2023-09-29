from celery import shared_task
from ronglianyunapi import send_sms as sms

# 记录日志
import logging

logger = logging.getLogger("django")


@shared_task(name="send_sms")
def send_sms(tid, mobile, datas):
    """异步发送短信"""
    try:
        return sms(tid, mobile, datas)
    except Exception as e:
        logger.error(f"手机号：{mobile}，发送短信失败错误：{e}")


@shared_task(name="send_sms1")
def send_sms1():
    print("send_sms1执行了！")
    return "send_sms1执行了！"


"""
关于celery中异步任务发布的2个方法参数如下：
异步任务名.delay(*arg, **kwargs)
异步任务名.apply_async((arg,), {'kwarg':value}, countdown=60, expires=120)

定时任务的调用器启动，可以在运行了worker以后，使用以下命令：
cd ~/Desktop/luffycity/luffycityapi
celery -A luffycityapi beat
beat调度器关闭了，则定时任务无法执行，如果worker工作进程关闭了，则celery关闭，保存在消息队列中的任务就会囤积在那里。
"""