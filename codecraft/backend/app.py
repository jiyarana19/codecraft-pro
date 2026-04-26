from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_feedback import get_feedback

app = Flask(__name__)
CORS(app)  # IMPORTANT

@app.route("/")
def home():
    return "Backend is working!"

@app.route("/evaluate", methods=["POST"])
def evaluate():
    try:
        data = request.get_json()
        code = data.get("code", "")

        feedback = get_feedback(code)

        return jsonify({"feedback": feedback})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"feedback": "Backend error!"})

if __name__ == "__main__":
    app.run(debug=True)