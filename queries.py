from main_db import session
from base import messages
import json
from sqlalchemy.orm.exc import NoResultFound
from response_ import chat_session

start =  session.query(messages.id_).order_by(messages.id_.desc()).first()
start = int((list(start))[0])


#Function to update Title after some conversation
def update_title(data, id_no):
    query = "This is the conversation between bot and user, based on this conversation just give me the title, just title, thats it"
    prompt = str(data) + query
    response = chat_session.send_message(prompt)
    new_title = response.text
    
    message_record = session.query(messages).filter_by(id_= id_no).one()
    message_record.title = new_title

    session.add(message_record)
    session.commit()


#function to add conversation in the database
def updating_data(new_data, id_no):

    try:

        value = str(id_no)  # assuming `id_` is a string

        # Use a database query to check if the value exists
        exists = session.query(messages.id_).filter(messages.id_ == value).first() is not None

        if exists == False:
            message = messages(id_no, {})
            session.add(message)
            session.commit()

        #to change the title after some conversatoin
        Titles = session.query(messages.title).filter(messages.id_ == id_no)

        for title in Titles:
            if list(title) == ["new_chat"]:
                conversation = session.query(messages.chat_message).filter(messages.id_ == id_no)
                
                for data in conversation:
                    data = list(data)[0]
            
                    if len(data) > 2:
                        update_title(data, id_no)

        # Fetch the message record by session_id
        message_record = session.query(messages).filter_by(id_= id_no).one()

        # Merging new data with the existing json_data in the database
        existing_data = message_record.chat_message
        if existing_data is None:
            existing_data = {}  # Initialize if None

        existing_data.update(new_data)  # Update the existing json_data with new data
        message_record.chat_message = json.loads(json.dumps(existing_data))

        session.add(message_record)

        session.commit()
        print("Data updated successfully.")

    except NoResultFound:
        print("No record found with the given ID.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

def get_data(id_no):
    data = session.query(messages.chat_message, messages.title).filter(messages.id_==id_no)
    return data
