def create_tables_db(my_sql):
    cursor = my_sql.connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(255) NOT NULL
        )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS task (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(50) NOT NULL,
            description TEXT,
            status VARCHAR(13) DEFAULT 'not done',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            id_user INT NOT NULL,
            FOREIGN KEY(id_user) REFERENCES user(id)
        )''')

    my_sql.connection.commit()
    cursor.close()
