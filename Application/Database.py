import pymysql


def init_database() -> pymysql.Connection:
    db = pymysql.connect(
        host='localhost',
        user='Blackboard',
        passwd='7355608',
        port=3306,
        db='Accounts'
    )
    print('Database Connected')
    return db


def add_account(account: str, password: str, db: pymysql.Connection) -> bool:
    cursor = db.cursor()
    sql = 'SELECT * FROM Accounts WHERE account = %s'
    cursor.execute(sql, (account,))
    result = cursor.fetchall()
    if len(result) == 0:
        sql = '''
        INSERT INTO Accounts (account, password)
        VALUES ((%s), (%s))
        '''
    elif len(result) == 1:
        sql = '''
        UPDATE Accounts SET password = %s WHERE account = %s
        '''

    cursor.execute(sql, (account, password,))
    db.commit()
    return True


def delete_account(account: str, db: pymysql.Connection) -> bool:
    cursor = db.cursor()
    sql = 'SELECT * FROM Accounts WHERE account = %s'
    cursor.execute(sql, (account,))
    result = cursor.fetchall()
    if len(result) > 0:
        sql = 'DELETE FROM Accounts WHERE account = %s'
        cursor.execute(sql, (account,))
        db.commit()
    return True


def check_password(account: str, db: pymysql.Connection) -> str:
    cursor = db.cursor()
    sql = 'SELECT * FROM Accounts WHERE account = %s'
    cursor.execute(sql, (account,))
    result = cursor.fetchall()
