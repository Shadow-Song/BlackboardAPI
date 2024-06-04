import pymysql

connection = pymysql.connect(
    host='localhost',
    user='Blackboard',
    password='7355608',
    database='Accounts',
)

cursor = connection.cursor()


def init_database():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Accounts (
        username VARCHAR(255) NOT NULL PRIMARY KEY,
        password VARCHAR(255) NOT NULL
    );
    ''')
    connection.commit()


def get_user(username: str):
    cursor.execute(f'SELECT * FROM Accounts WHERE username = "{username}"')
    user = cursor.fetchone()
    return user


def get_all_users():
    cursor.execute('SELECT * FROM Accounts')
    users = cursor.fetchall()
    return users


def update_user(username: str, password: str):
    exists = get_user(username)
    if exists:
        cursor.execute(f'UPDATE Accounts SET password = "{password}" WHERE username = "{username}"')
    else:
        cursor.execute(f'INSERT INTO Accounts (username, password) VALUES ("{username}", "{password}")')
    connection.commit()


def delete_user(username: str):
    cursor.execute(f'DELETE FROM Accounts WHERE username = "{username}"')
    connection.commit()


def close():
    connection.close()
