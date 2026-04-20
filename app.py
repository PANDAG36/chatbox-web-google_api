from flask import Flask, render_template, request
from chatbox import chatresponse

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_text = request.form.get("input_text")
        response,model = chatresponse(user_text)

        chat_history.append({"role": "user", "text": user_text})
        chat_history.append({"role": "bot", "text": f"'GEMINI': {response}"})

    return render_template("index.html", chat=chat_history,model=model)

if __name__ == "__main__":
    app.run(debug=True)