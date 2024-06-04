import requests
import urllib3
import base64

from Database import Database
from Security import Security


urllib3.disable_warnings()
Database.init_database()


def encode_base64(message: str) -> str:
    # 将字符串转换为字节串
    message_bytes = message.encode('utf-8')
    # 使用base64加密
    base64_bytes = base64.b64encode(message_bytes)
    # 将加密后的字节串转换为字符串
    base64_message = base64_bytes.decode('utf-8')
    return base64_message


def login(username, password):
    # Blackboard Helper 登录接口
    url = 'https://bbh.yangyq.net/login'
    body = {
        "username": username,
        "password": encode_base64(password)
    }

    response = requests.post(url, json=body, verify=False).json()
    if response['code'] == 20000:
        # 登录成功，在数据库中更新密码
        Database.update_user(username, password)
        # 返回RSA加密后的session
        session = response['data']['session']
        print(Security.encrypt(session))
        return {'code': 200, 'session': Security.encrypt(session)}
    else:
        # 返回错误信息
        message = response['msg']
        return {'code': 400, 'message': message}


def logout(username):
    # 从数据库中删除关于这个用户的信息
    Database.delete_user(username)
    return {'code': 200, 'message': 'Logout Successfully'}


def refresh_session(username):
    # 查找用户
    user = Database.get_user(username)
    if not user:
        return {'code': 400, 'message': 'User Not Found'}
    else:
        password = user[1]
        login(username, password)
        return {'code': 200, 'session': Database.get_user(username)[2]}
