from main_db import session
from base import messages

data = session.query(messages.chat_message, messages.title).filter(messages.id_)

def getting_titles():
    for title in data:
        yield title[1].replace("\n", "")

def msg_index():
    for i in data:
        messages = list(i)[0]
        key_data = [i for i, _ in messages.items()]
# print(key_data)

    return int(key_data[-1])   