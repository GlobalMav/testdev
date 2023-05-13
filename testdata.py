import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)
redis.set('RUR', '1')
redis.set('USD', '42')
redis.set('KZ', '100')


keys = redis.keys()

for key in keys:
    print(key, redis.get(key))
