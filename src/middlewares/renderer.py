import datetime
import json

from aiohttp import web

STATUS_MESSAGES = {
    200: 'Status OK',
    201: 'Created',
    202: 'Updated',
    204: 'Deleted',
    400: 'Bad Request',
    403: 'Forbidden',
    404: 'Not Found',
    500: 'Internal Server Error',

}


async def get_logs(req: web.Request):
    data = dict()
    data['host'] = req.host
    data['path'] = req.path
    data['method'] = req.method
    data['headers'] = req.headers
    data['content-type'] = req.content_type
    data['body'] = await req.json() if req.body_exists else None
    data['time'] = datetime.datetime.utcnow()
    return data


@web.middleware
async def render(request: web.Request, handler: web.Callable) -> web.Response:
    if request.method == "OPTIONS":
        return web.json_response({"success": True}, status=200)
    print(await get_logs(request))
    response = await handler(request)
    resp_data = {'success': response.status // 100 not in (4, 5)}
    if resp_data['success']:
        data = json.loads(response.body)
        if isinstance(data, dict):
            if data.get('message'):
                resp_data['message'] = data['message']
                del data['message']
            else:
                resp_data['message'] = STATUS_MESSAGES[response.status]

            if data.get('data'):
                resp_data['data'] = data['data']
    else:
        resp_data['message'] = response.text if response.text else STATUS_MESSAGES[response.status]
        try:
            data = json.loads(response.body)
            if 'message' in data:
                resp_data['message'] = data['message']
            if 'errors' in data:
                resp_data['errors'] = data['errors']
        except Exception as e:
            print(e)

    return web.json_response(data=resp_data, status=response.status)

