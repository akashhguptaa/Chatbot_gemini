from main_db import session
from base import messages
from flask import render_template, url_for, Flask, request, Response
from response_ import model

import json

def old_memory(old_messages):
    chat_session = model.start_chat(
        history=[

        ]
    )
    query = "This is the conversation between a bot and user now based on that answer the next questions"
    response = chat_session.send_message( query + old_messages)
    
app = Flask(__name__)

# Convert value to the same type as in the database
id_no = "1008"  # assuming `id_` is a string

# Use a database query to check if the value exists
data = session.query(messages.chat_message, messages.title).filter(messages.id_ == 1003)
# count = 0
def gemini_data(prompt, data_to_db):
    response = chat_session.send_message(prompt, stream=True)
    for chunks in response:
        data  = chunks.text.replace("*", "")
        yield data

    #adding bot response to database
    data_to_db[count]["User"] = prompt
    data_to_db[count]["Bot"] = response.text.replace("*", "")
    
    #Adding data to database
    updating_data(data_to_db, start)
    
@app.route("/")
def for_1004():
    for i in data:
        # count += 1
        old_messages = list(i)[0]
        old_memory(old_messages)
        return render_template('old_chats.html', old_messages = old_messages)

@app.route("/get")
def get_bot_response():

    global count

    count +=  1
    userText = request.args.get('msg')

    data_to_db = {count : {}}
    
    message = [{"role": "user", "content": userText}]
    
    def generate():
        for response in bot_res(userText, data_to_db):
            yield f"data: {response}\n\n"

    return Response(generate(), content_type='text/event-stream')
if __name__ == "__main__":
    app.run(debug = True, port = 8000)




    






    
    
    
