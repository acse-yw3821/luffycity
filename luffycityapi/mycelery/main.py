# 1. 导入celery，创建应用对象
import os, django
from celery import Celery

# 初始化django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luffycityapi.settings.dev")
django.setup()

# 初始化celery对象
app = Celery("luffycity")

# 2. 加载配置
app.config_from_object("mycelery.settings")

# 3. 注册任务
# 参数必须是一个列表，里面的每个任务都是任务的路径名称
# app.autodiscover_tasks(["mycelery.sms", "mycelery.mail"])
app.autodiscover_tasks(["mycelery.sms"])

# 4. 终端下调用异步任务或者在其他项目中调用异步任务
# 启动Celery的终端命令
# 强烈建议切换目录到项目的根目录下启动celery!!
# celery -A mycelery.main worker --loglevel=info
