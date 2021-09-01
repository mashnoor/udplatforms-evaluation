
from configs.app_vars import DB_NAME
from pony.orm import *

db = Database()

db.bind(provider='sqlite', filename=DB_NAME, create_db=True)






