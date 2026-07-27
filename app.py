from flask import Flask, render_template, request, jsonify

from chat import CustomerSupportAssistant

app = Flask(__name__)

# One assistant instance shared by all requests (simple demo setup).
# self.memory inside it means all visitors share the same conversation history -
# fine for a local demo, not for multiple real users at once.
assistant = None
init_error = None

try:
    assistant = CustomerSupportAssistant()
except ValueError as e:
    init_error = str(e)


@app.route("/")
def home():
    return render_template("index.html", init_error=init_error)


@app.route("/chat", methods=["POST"])
def chat_endpoint():
    if assistant is None:
        return jsonify({"reply": f"Setup error: {init_error}"}), 500

    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    reply = assistant.process_message(message)
    return jsonify({"reply": reply})


@app.route("/clear", methods=["POST"])
def clear_endpoint():
    if assistant is not None:
        assistant.memory.clear()
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
