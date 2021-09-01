from users.models import User, Address
from pony.orm import db_session


@db_session
def user_serializer(user: User) -> dict:
    data = dict()

    data['id'] = user.id
    data['first_name'] = user.first_name
    data['last_name'] = user.last_name
    if user.type == User.Types.CHILD:
        print(user.id)
        parent_user = User.get(id=user.parent.id)
        data['address'] = address_serializer(parent_user.address)
        data['parent'] = user_serializer(parent_user)
    else:
        data['address'] = address_serializer(user.address)
    data['type'] = user.type

    return data


@db_session
def address_serializer(address: Address) -> dict:
    serialized_address = dict()
    serialized_address['street'] = address.street
    serialized_address['zip'] = address.zip
    serialized_address['city'] = address.city
    serialized_address['state'] = address.state

    return serialized_address
