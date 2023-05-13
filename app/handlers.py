from aiohttp import web


async def convert(request: web.Request) -> web.Response:
    query = request.rel_url.query

    return web.json_response(
        {
            "amount": 10,
        },
    )