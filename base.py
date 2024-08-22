from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import declarative_base
from main_db import session

Model = declarative_base()
Model.query = session.query_property()

class messages(Model):
    __tablename__ = "Messages"

    id_ = Column("ID", String, primary_key=True)
    chat_message = Column("Chat_Data", JSON)
    title = Column("Title", String, default= "new_chat")

    def __init__(self, id_, chat_messages, title = "new_chat"):
        self.id_ = id_
        self.chat_message = chat_messages
        self.title = title

    def __repr__(self):
        return f"({self.id_}) {self.chat_message   } ({self.title})"