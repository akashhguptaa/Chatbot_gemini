from flask import Flask, render_template, request, jsonify, Response, url_for
from response_ import gemini_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    message = [{"role": "user", "content": userText}]
    
    def generate():
        for response in gemini_data(userText):
            yield f"data: {response}\n\n"

    return Response(generate(), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
