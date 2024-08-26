from flask import Flask, render_template, request, Response
from response_ import chat_session
from queries import updating_data, start, get_data
from last_msg import msg_index
from main_db import session
from base import messages

app = Flask(__name__)

count = 0

#To generate the response
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

def old_memory(old_messages):
    
    query = "This is the conversation between a bot and user now based on that answer the next questions"
    response = chat_session.send_message( query + old_messages)

@app.route("/")
def home():
    global start 
    start += 1
    data = session.query(messages.chat_message, messages.title).filter(messages.id_)
    return render_template("index.html", data = data)


@app.route("/get")
def get_bot_response():

    global count

    count +=  1
    userText = request.args.get('msg')

    data_to_db = {count : {}}
    
    message = [{"role": "user", "content": userText}]
    
    def generate():
        for response in gemini_data(userText, data_to_db):
            yield f"data: {response}\n\n"

    return Response(generate(), content_type='text/event-stream')


msg_start = msg_index()

@app.route("/chat/<id_no>")
def for_1004(id_no):
    data = get_data(id_no)
    for i in data:
        msg_start += 1
        old_messages = list(i)[0]
        old_memory(str(old_messages))
        return render_template('old_chats.html', old_messages=old_messages, data= data)

if __name__ == "__main__":
    app.run(debug=True)
