from redis import Redis, StrictRedis

if __name__ == "__main__":
    # 连接redis的写法
    # 方法1. url="redis://:密码@IP:端口/数据库编号"
    redis = Redis.from_url(url="redis://:AlwaysDay1@127.0.0.1:6379/0")
    # redis = Redis(host="127.0.0.1", port=6379, password="AlwaysDay1", db=0)

    # 字符串
    # set name xiaoming
    # redis.set("name", "xiaoming")
    #
    # # setex sms_13312345678 30 500021
    # redis.setex("sms_13312345678", 30, "500021")
    #
    # ret = redis.get("sms_13312345678")
    # # redis中最基本的数据类型是字符串，但是这种字符串是bytes，所以对于python而言，读取出来的字符串数据还要decode才能使用
    # print(ret, ret.decode())
    #
    # # 提取数据，键如果不存在，则返回结果为None
    # code_bytes = redis.get("sms_11")
    # print(code_bytes)
    # if code_bytes:
    #     print(code_bytes.decode())
    #
    # # 设置字典，多个成员
    # # hset user name xiaohong age 12 sex 1
    # data = {
    #     "name": "xiaobing",
    #     "age": 12,
    #     "sex": 1
    # }
    # redis.hset("user", mapping=data)
    # # 获取字典所有成员，字典的所有成员都是键值对，而键值对也是bytes类型，所以需要推导式进行转换
    # ret = redis.hgetall("user")
    # print(ret)
    # data = {key.decode(): value.decode() for key, value in ret.items()}
    # print(data)
    #
    # ret = redis.hget("user", "name")
    # print(ret)

    # 获取当前仓库的所有keys
    ret = redis.keys("*")
    print(ret)

    # # 删除key
    if len(ret) > 0:
        redis.delete(ret[0])
