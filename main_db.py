from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine("sqlite:///chat_bot.db", echo=True)

session = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )
)

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA forign_key=ON")
    cursor.close()



# try:
#     # Fetch the message record by session_id
#     message_record = session.query(messages).filter_by(id_=1001).one()
    
#     # Update the json_data
#     new_data = {
#         2: {"User": "tell me about humans?", "Bot": "Humans are kind"}
#     }
    
#     # Merging new data with the existing json_data in the database
#     existing_data = message_record.chat_messages
#     if existing_data is None:
#         existing_data = {}  # Initialize if None
#     print(f"\n\n{existing_data}\n\n")
#     existing_data.update(new_data)  # Update the existing json_data with new data
    
#     print(f"\n\n{existing_data}\n\n")
#     # Assign the updated data back to the record
#     message_record.chat_messages = existing_data
    
#     # Commit the changes to the database
#     session.commit()
#     print("Data updated successfully.")

# except NoResultFound:
#     print("No record found with session_id=1001. Please check the session_id.")
#     session.rollback()

# except sqlalchemy.exc.IntegrityError as e:
#     print(f"Integrity error occurred: {e}")
#     session.rollback()

# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#     session.rollback()



# print("Hello world")
         
