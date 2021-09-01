import json

from aiohttp.web_request import Request
from aiohttp import web
from users.models import User, Address
from users.serializers import user_serializer
from pony.orm import db_session, commit


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

    if first_name and last_name and user_type:
        if user_type == User.Types.PARENT:
            if street and city and state and zip_no:
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
                return web.HTTPBadRequest(text='invalid request payload')


        elif user_type == User.Types.CHILD and parent_id:
            with db_session:
                parent_user = User.get(id=parent_id)
                if not parent_user:
                    return web.HTTPNotFound(text="parent user not found")

                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    type=User.Types.CHILD,
                    parent=parent_user,
                )
                commit()
    else:
        return web.HTTPBadRequest(text='invalid request payload')

    response_data = dict()
    response_data['message'] = "User created successfully"
    response_data['data'] = user_serializer(new_user)
    print(user_serializer(new_user))
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

    # try:
    if user_id:
        with db_session:
            user = User.get(id=user_id)
            if not user:
                return web.HTTPNotFound(text="user not found")
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if parent_id and user.type == User.Types.CHILD:
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
        print(user_serializer(user))
        return web.json_response(data=response_data, status=200)

    return web.HTTPBadRequest(text="'user_id' is required")


async def delete(request: Request) -> web.Response:
    user_id = request.query.get('id')
    if user_id:
        with db_session:
            user = User.get(id=user_id)
            if not user:
                return web.HTTPNotFound(text="user not found")

            user.delete()
            return web.json_response(data={"message": "user deleted successfully"}, status=204)