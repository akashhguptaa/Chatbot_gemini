from flask import Flask, render_template, request, Response
from response_ import chat_session
from queries import updating_data
from queries import start

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

@app.route("/")
def home():
    global start 
    start += 1
    return render_template("index.html")


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

if __name__ == "__main__":
    app.run(debug=True)
