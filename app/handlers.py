from aiohttp import web
from aiohttp_session import get_session
import aioredis
import json


async def convert(request: web.Request) -> web.Response:
    redis = aioredis.from_url("redis://localhost")
    query = request.rel_url.query
    val1, val2 = query.get('from'), query.get('to')
    amount = int(query.get('amount'))
    val1cost, val2cost = (await redis.get(val1)), (await redis.get(val2))
    amount = (amount*int(val1cost))/int(val2cost)
    return web.json_response(
        {
            "amount": amount
        },
    )

async def datamerge(request: web.Request) -> web.Response:
    redis = aioredis.from_url("redis://localhost")
    query = request.rel_url.query
    data = await request.json()
    merge = query.get('merge')
    print(merge)
    if merge == '0':
        for key in await redis.keys('*'):
            await redis.delete(key)
        for key, value in data.items():
            await redis.set(key, value)
    elif merge == '1':
        for key, value in data.items():
            await redis.set(key, value)
    else:
        return web.Response(status=400, text='Invalid merge value')
    return web.json_response(
        {
            "message": "Data merge successful"
        },
    )
