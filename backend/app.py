from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from db_config import init_db
from db_model import create_tables_db
from werkzeug.security import generate_password_hash

app = Flask(__name__)

my_sql = init_db(app)

with app.app_context():
    create_tables_db(my_sql)

@app.route("/")
def home():
    return jsonify(message="Hello World")
#*************************************************************************************************************************************************************#
# Task ENDPOINTS

# Create Task Endpoint
@app.route("/task", methods=['POST'])
def create_task():
    return jsonify({"message": "Task created successfully"}), 201

# Update Task Endpoint
@app.route("/task", methods=['PUT'])
def update_task():
    return jsonify(message="Task updated")

# Get Task By Id Endpoint
@app.route("/task", methods=['GET'])
def get_task_by_id():
    return jsonify(message="Task selected")

# Get all tasks Endpoint
@app.route("/task/all", methods=['GET'])
def get_all_tasks():
    return jsonify(message="All Tasks")

# Delete Task Endpoint
@app.route("/task", methods=['DELETE'])
def delete_task_by_id():
    return jsonify(message="Task deleted")

#*************************************************************************************************************************************************************#
# User ENDPOINTS

# Register User Endpoint
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    name = data['name']
    username = data['username']
    password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    cursor = my_sql.connection.cursor()
    cursor.execute('''
        INSERT INTO user (name, username, password)
        VALUES (%s, %s, %s)
    ''', (name, username, password))
    my_sql.connection.commit()
    cursor.close()

    return jsonify({"message": "User registered successfully"}), 201

# Login Endpoint
@app.route('/login', methods=['POST'])
def login_user():
    return jsonify ({"message":"Login done successfuly"})

if __name__ == "__main__":
    app.run(debug=True)