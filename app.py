from flask import Flask, render_template, request, jsonify
from response_ import gemini_data

app = Flask(__name__)

def get_completion(prompt):
    message = [{"role": "user", "content": prompt}]
    response = gemini_data(prompt)
    return response

@app.route("/")
def  home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = get_completion(userText)
    return response

if __name__ == "__main__":
    app.run()