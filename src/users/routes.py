from aiohttp import web
from users.views import create, update, delete

routes = [
    web.post('/api/v1/user', create),
    web.put('/api/v1/user', update),
    web.delete('/api/v1/user', delete),
]

user_routes = routes
