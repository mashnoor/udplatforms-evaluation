from aiohttp import web
from aiohttp.web_request import Request
from pony.orm import db_session, commit

from users.models import User, Address
from users.serializers import user_serializer
import logging
from users.validators import is_valid_id

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create(request: Request) -> web.Response:
    body = await request.json()
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    user_type = body.get('user_type')
    street = body.get('street')
    city = body.get('city')
    state = body.get('state')
    zip_no = body.get('zip')
    parent_id = body.get('parent_id')

    if not first_name or not last_name or not user_type:
        return web.HTTPBadRequest(text='Valid first_name, last_name and user_type is required')

    if user_type not in (User.Types.PARENT, User.Types.CHILD):
        return web.HTTPBadRequest(text='Invalid user type')

    if user_type == User.Types.PARENT:
        if not street or not city or not state or not zip_no:
            return web.HTTPBadRequest(text="Valid street, city, state, zip_no is required for parent")
        with db_session:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                type=User.Types.PARENT
            )
            Address(
                user=new_user,
                street=street,
                city=city,
                state=state,
                zip=zip_no,
            )

    else:
        if not parent_id or not is_valid_id(parent_id):
            return web.HTTPBadRequest(text="invalid parent_id")
        with db_session:
            parent_user = User.get(id=parent_id)
            if not parent_user:
                return web.HTTPNotFound(text="Parent user not found")

            if parent_user.type == User.Types.CHILD:
                return web.HTTPNotAcceptable(text='Child cannot be a parent of another child')

            new_user = User(
                first_name=first_name,
                last_name=last_name,
                type=User.Types.CHILD,
                parent=parent_user,
            )
            commit()

    response_data = dict()
    response_data['message'] = "User created successfully"
    response_data['data'] = user_serializer(new_user)
    return web.json_response(data=response_data, status=201)


async def update(request: Request) -> web.Response:
    body = await request.json()
    user_id = request.query.get('id')
    first_name = body.get('first_name')
    last_name = body.get('last_name')
    street = body.get('street')
    city = body.get('city')
    state = body.get('state')
    zip_no = body.get('zip')
    parent_id = body.get('parent_id')

    if not user_id or not is_valid_id(user_id):
        return web.HTTPBadRequest(text='invalid user_id')

    with db_session:
        user = User.get(id=user_id)
        if not user:
            return web.HTTPNotFound(text="user not found")
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if parent_id and is_valid_id(parent_id) and user.type == User.Types.CHILD:
            user.parent = User.get(id=parent_id)
        if user.type == User.Types.PARENT:
            user_address: Address = user.address
            if street:
                user_address.street = street
            if city:
                user_address.city = city
            if state:
                user_address.state = state
            if zip_no:
                user_address.zip = zip_no

        response_data = dict()
        response_data['message'] = "User updated successfully"
        response_data['data'] = user_serializer(user)
        return web.json_response(data=response_data, status=200)


async def delete(request: Request) -> web.Response:
    user_id = request.query.get('id')
    if not user_id or not is_valid_id(user_id):
        return web.HTTPNotAcceptable(text='Invalid id provided')

    with db_session:
        user = User.get(id=user_id)
        if not user:
            return web.HTTPNotFound(text="User not found")

        user.delete()
        return web.json_response(data={"message": "User deleted successfully"}, status=200)
