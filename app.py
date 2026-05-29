from flask import Flask, render_template, request, jsonify
from chatbot import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question")
    answer = chatbot(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
