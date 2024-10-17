from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from db_config import init_db
from db_model import create_tables_db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 's3cr3t_k3y'
jwt = JWTManager(app)

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
@jwt_required()
def create_task():
    data = request.json
    title = data['title']
    description = data['description']
    user_id = get_jwt_identity()

    cursor = my_sql.connection.cursor()
    cursor.execute('''
        INSERT INTO task (title, description, id_user)
        VALUES (%s, %s, %s)
    ''', (title, description, user_id))
    my_sql.connection.commit()
    cursor.close()

    return jsonify({"message": "Task created successfully"}), 201

# Update Task Endpoint
@app.route("/task", methods=['PUT'])
def update_task():
    return jsonify(message="Task updated")

# Get Task By Id Endpoint
@app.route("/task/<int:id>", methods=['GET'])
@jwt_required()
def get_task_by_id(id):
    cursor = my_sql.connection.cursor()
    cursor.execute("SELECT * FROM task WHERE id=%s", (id,))
    task = cursor.fetchone()
    cursor.close()

    if not task:
        return jsonify({"message": "Task not found"}), 404

    task_data = {
        'id': task[0],
        'title': task[1],
        'description': task[2],
        'status': task[3],
        'created_at': task[4]
    }
    return jsonify(task_data), 200

# Get all tasks Endpoint
@app.route("/task/all", methods=['GET'])
@jwt_required()
def get_all_tasks():
    cursor = my_sql.connection.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    cursor.close()

    task_list = []
    for task in tasks:
        task_list.append({
            'id': task[0],
            'title': task[1],
            'description': task[2],
            'status': task[3],
            'created_at': task[4]
        })
    return jsonify(task_list), 200

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
    data = request.json
    username = data['username']
    password = data['password']

    cursor = my_sql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
    user = cursor.fetchone()
    cursor.close()

    if user is None or not check_password_hash(user[3], password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user[0])

    return jsonify({"token": access_token}), 200

if __name__ == "__main__":
    app.run(debug=True)