from flask import Flask, render_template, request, jsonify, Response, url_for
from response_ import chat_session
from add_data import botData_db, userData_db
from Db_creation import messages, session

app = Flask(__name__)

start = session.query(messages).filter(messages.id_) 
for data in start:
    print("here i amm please look at me\n\n\n",start)
count = 0
def gemini_data(prompt):
    response = chat_session.send_message(prompt, stream=True)
    for chunks in response:
        data  = chunks.text.replace("*", "")
        yield data

    #adding bot response to database
    botData_db(response.text.replace("*", ""), count)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    # print(chat_data)
    global count
    count +=  1
    userText = request.args.get('msg')

    #adding userData to database
    userData_db(userText, count)
    
    message = [{"role": "user", "content": userText}]
    
    def generate():
        for response in gemini_data(userText):
            yield f"data: {response}\n\n"

    return Response(generate(), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
