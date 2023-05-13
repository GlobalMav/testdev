from aiohttp import web

from containers import Container
import handlers


def create_app() -> web.Application:
    container = Container()

    app = web.Application()
    app.container = container
    app.add_routes([
        web.get("/convert", handlers.convert),
    ])
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)