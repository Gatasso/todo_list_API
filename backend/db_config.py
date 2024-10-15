from app import app
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql123'
app.config['MYSQL_DB'] = 'db_todo_list'
