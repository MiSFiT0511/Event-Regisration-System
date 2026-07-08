from flask import Flask, request, jsonify, render_template

import database
import backend

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name", "")
    age = data.get("age", "")
    email = data.get("email", "")

    result = backend.register_participant(name, age, email)

    return jsonify(result)

@app.route("/participants", methods=["GET"])
def participants():

    rows = database.view_participants()

    result = []

    for r in rows:
        result.append({
            "id": r[0],
            "name": r[1],
            "age": r[2],
            "email": r[3]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)