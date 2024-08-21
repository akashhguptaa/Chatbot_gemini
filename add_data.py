from main_db import session
from base import messages
import sqlalchemy
import json
from sqlalchemy.orm.exc import NoResultFound


def updating_data(new_data):

    try:
        # Fetch the message record by session_id
        message_record = session.query(messages).filter_by(id_=1001).one()

        # Merging new data with the existing json_data in the database
        existing_data = message_record.chat_message
        if existing_data is None:
            existing_data = {}  # Initialize if None

        existing_data.update(new_data)  # Update the existing json_data with new data
        message_record.chat_message = json.loads(json.dumps(existing_data))

        session.add(message_record)
        # session.flush()

        session.commit()
        print("Data updated successfully.")

    except NoResultFound:
        print("No record found with the given ID.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
# updating_data({4:{"User":  "adfkanjka", "Bot": "afnajkfka"}})
