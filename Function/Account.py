import requests
import re
from Model.Login import LoginResponse


def login(account: str, password: str) -> LoginResponse:
    print("Logging in...")
    url = 'https://id.ouc.edu.cn/baseLogin/postLogin'
    body = {
        'account': account,
        'password': password,
        'randomCode': 'comsys-base-login',
        'isRememberPwdOpen': 0,
        'scale': 1
    }

    response = requests.post(url, json=body, verify=False)
    json = response.json()
    code = json['code']
    if code == 200:
        cookie = response.headers['Set-Cookie']
        match = re.search(r'JSESSIONID=([^;]+)', cookie)
        session = match.group(1)
        token = json['datas']['casUser']['token']
        identity_id = json['datas']['casUser']['identityId']
        name = json['datas']['casUser']['personName']
        json = {
            'session': session,
            'token': token,
            'identityId': identity_id,
            'name': name
        }
        return LoginResponse(code=200, msg='success', data=json)

    else:
        msg = json['msg']
        return LoginResponse(code=code, msg=msg, data={})
