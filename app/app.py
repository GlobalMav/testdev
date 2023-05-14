from aiohttp import web
from aiohttp_session import get_session, session_middleware
from aiohttp_session.redis_storage import RedisStorage
import aioredis
from containers import Container
import handlers
from urllib.parse import urlparse
from types import MappingProxyType


def create_app() -> web.Application:
    container = Container()
    app = web.Application()
    app.container = container
    app.add_routes([
        web.get("/convert", handlers.convert),
        web.post("/database", handlers.datamerge)
    ])
    return app



if __name__ == "__main__":
    app = create_app()
    web.run_app(app, port=8000)

