from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message= "Hello World")

@app.route("/task", methods=['POST'])
def create_task():
    return jsonify(message= "Task created")

@app.route("/task", methods=['PUT'])
def update_task():
    return jsonify(message= "Task updated")

@app.route("/task", methods=['GET'])
def get_task_by_id():
    return jsonify(message= "Task selected")

@app.route("/task/all", methods= ['GET'])
def get_all_tasks():
    return jsonify(message= "All Tasks")

@app.route("/task", methods=['DELETE'])
def delete_task_by_id():
    return jsonify(message= "Task deleted")


if __name__ == "__main__":
    app.run(debug=True)