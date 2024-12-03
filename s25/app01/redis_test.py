# import redis

# 方式一 不推荐 直接连接redis
# conn = redis.Redis(host='ip',port='6379', password='1111111', encoding='utf-8')

# 设置键值 18553971111=“9999”且超时时间为10秒（值写入到redis时会自动转字符串）
# conn.set('18553971111', 9999, ex=10)

# 根据键获取值：如果存在获取值（获取到的是字节类型）； 不存在则返回None
# value = conn.get('18553971111')

# print(value)


# 方式二 （推荐）创建redis连接池（默认连接池做大连接数 2**31 = 21478483648）
# pool = redis.ConnectionPool(host='ip',port='6379', password='111111', encoding='utf-8', max_connections=1000)

# 去连接池中获取一个连接
# conn = redis.Redis(connection_pool=pool)

# 设置键值，10秒
# conn.set('name', '张三', ex=10)

# 根据键获取值：如果存在获取值（获取到的是字节类型）； 不存在则返回None
# value = conn.get('name')

# print(value)


from django.shortcuts import HttpResponse

from django_redis import get_redis_connection

def index(request):
    # 去连接池中获取一个连接
    conn = get_redis_connection() # 不写默认连接'default'
    
    conn.set('nickname', '张三', ex=10)
    value = conn.get('nickname')
    print(value)
    return HttpResponse('ok')