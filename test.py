from main_db import session
from base import messages
import sqlalchemy
import json
from sqlalchemy.orm.exc import NoResultFound

# Convert value to the same type as in the database
value = "1003"  # assuming `id_` is a string

# Use a database query to check if the value exists
exists = session.query(messages.id_).filter(messages.id_ == value).first() is not None
print(type(exists))
if exists == True:
    print("yes")
else:
    print("no")
