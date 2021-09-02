from configs import *


class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    address = Optional("Address", nullable=True, cascade_delete=True)
    type = Required(str)
    parent = Optional("User", nullable=True, reverse='children')
    children = Set('User', nullable=True, reverse='parent', cascade_delete=True)

    class Types:
        PARENT = "parent"
        CHILD = "child"


class Address(db.Entity):
    _table_ = "addresses"
    user = Required("User", reverse="address")
    street = Required(str)
    city = Required(str)
    state = Required(str)
    zip = Required(int)


db.generate_mapping(create_tables=True)
