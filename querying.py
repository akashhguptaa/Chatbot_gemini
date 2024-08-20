from main_db import session
from base import messages
import sqlalchemy
import json
from sqlalchemy.orm.exc import NoResultFound

try:
    # Fetch the message record by session_id
    message_record = session.query(messages).filter_by(id_=1001).one()

    # New data to be added
    new_data = {2: {"User": "tell me about humans?", "Bot": "Humans are kind"}}

    # Merging new data with the existing json_data in the database
    existing_data = message_record.chat_message
    if existing_data is None:
        existing_data = {}  # Initialize if None
    print(f"earler: {existing_data}\n\n")
    existing_data.update(new_data)  # Update the existing json_data with new data
    print(f"After: {existing_data}\n\n")

    # Assign the updated data back to the record
    message_record.chat_message = json.loads(json.dumps(existing_data))
    print("--- ", message_record.chat_message)
    message_record.title = "akash_introduction"

    # Explicitly add the record back to the session and flush changes
    session.add(message_record)
    # session.flush()

    # Commit the transaction
    session.commit()
    print("Data updated successfully.")

except NoResultFound:
    print("No record found with the given ID.")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()
