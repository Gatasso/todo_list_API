from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    # Configurações do banco de dados
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'mysql123'
    app.config['MYSQL_DB'] = 'db_todo_list'
    
    # Inicializa o MySQL no app
    mysql.init_app(app)