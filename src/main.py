from aiohttp import web
from aiohttp_middlewares import cors_middleware

from middlewares import render
from users.routes import user_routes

app = web.Application(middlewares=[cors_middleware(allow_all=True), render])


async def health_check(request):
    data = {
        "message": "udplatform assigment health check",
        "method": request.method
    }

    return web.json_response(data=data, status=200)


app.add_routes([web.get('/', health_check)])
app.add_routes(user_routes)

web.run_app(app, port=8030)
