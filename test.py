from main_db import session
from base import messages
from response_ import chat_session


# Convert value to the same type as in the database
id_no = "1008"  # assuming `id_` is a string

# Use a database query to check if the value exists
titles = session.query(messages.title).filter(messages.id_ == 1008)

for title in titles:
    if list(title) == ["new_chat"]:
        conversation = session.query(messages.chat_message).filter(messages.id_ == 1008)
                
        for data in conversation:
            data = (list(data))[0]
            # print(len(data))
            if len(data) > 2:
                print("data is not updating\n\n")

                query = "This is the conversation between bot and user, based on this conversation just give me the title, just title, thats it"
                prompt = str(data) + query
                response = chat_session.send_message(prompt)
                new_title = response.text
                
                message_record = session.query(messages).filter_by(id_= 1008).one()
                message_record.title = new_title
                print(new_title)
                session.add(message_record)
                session.commit()
            

# query = "This is the conversation between bot and user, based on this conversation just give me the title, just title, thats it"
# for message in titles:
#     message = list(message)[0]
#     prompt = str(message) + query
#     if len(message) > 2:
#         response = chat_session.send_message(prompt)
#         print(response.text)

#     else:
#         print("chota hai")




    
    
    
