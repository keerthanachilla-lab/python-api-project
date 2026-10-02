
app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return jsonify({"message": "Python API is running successfully!"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or "task" not in data:
        return jsonify({"error": "Task is required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "task": data["task"]
    }

    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(debug=True)
