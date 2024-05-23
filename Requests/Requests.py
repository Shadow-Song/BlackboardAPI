import requests
import re


def login(account: str, password: str):
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
        return {'code': 200, 'msg': 'success', 'data': json}

    else:
        msg = json['msg']
        return {'code': code, 'msg': msg, 'data': {}}


def get_user_id(account: str, session_id: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/users?userName={account}'
    headers = {
        'Cookie': f's_session_id={session_id};',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'xweb_xhr': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
    }

    response = requests.get(url, headers=headers, verify=False).json()
    if 'code' in response:
        return {'code': response['code'], 'msg': response['message']}
    elif 'results' in response:
        return {
            'code': 200, 
            'msg': 'success', 
            'id': response['results'][0]['id'], 
            'name': response['results'][0]['name']['given'],
            'college': response['results'][0]['name']['family']
        }
    return {'code': 400, 'msg': 'Unknown Error'}


def get_calendar(session_id: str):
    url = 'https://wlkc.ouc.edu.cn/learn/api/public/v1/calendars/items'
    headers = {
        'Cookie': f's_session_id={session_id};',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'xweb_xhr': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
    }

    response = requests.get(url, headers=headers, verify=False)
    # print(response.json())
    if response.json()['status'] == 401:
        return {'code': 401, 'msg': 'Unauthorized'}
    return response.json()['results']


def get_course_list(user_id: str, s_session_id: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/users/{user_id}/courses'
    headers = {
        'xweb_xhr': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': f's_session_id={s_session_id}'
    }
    courses = []
    response = requests.request("GET", url, headers=headers).json()
    if 'code' in response:
        return response
    elif 'results' in response:
        for course in response['results']:
            if course['availability']['available'] == 'Yes' and course['courseRoleId'] == 'Student':
                courses.append(course['id'])
        return {'result': courses}

    return {'code': 400, 'msg': 'Unknown Error'}