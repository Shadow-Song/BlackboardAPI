import requests


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
