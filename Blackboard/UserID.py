import requests
import urllib3


urllib3.disable_warnings()


def get_user_id(account: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/users?userName={account}'
    header = {
        'xweb_xhr': 1,
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': session
    }
    response = requests.get(url, headers=header, verify=False).json()
    if response['status'] == 401:
        return {'code': 401, 'msg': 'Unauthorized'}
    else:
        user_id = response['results'][0]['id']
        name = response['results'][0]['name']['given']
        college = response['results'][0]['name']['family']
        return {'code': 200, 'user_id': user_id, 'name': name, 'college': college}


def get_user_name(user_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/users/{user_id}'
    header = {
        'xweb_xhr': 1,
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': session
    }
    response = requests.get(url, headers=header, verify=False).json()
    if response['status'] == 401:
        return {'code': 401, 'msg': 'Unauthorized'}
    elif response['status'] == 404:
        return {'code': 404, 'msg': 'User Not Found'}
    else:
        name = response['name']['given']
        college = response['name']['family']
        return {'code': 200, 'name': name, 'college': college}


def get_course_list(user_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/users/{user_id}/courses'
    header = {
        'xweb_xhr': 1,
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': session
    }
    response = requests.get(url, headers=header, verify=False).json()
    if response['status'] == 401:
        return {'code': 401, 'msg': 'Unauthorized'}
    elif response['status'] == 404:
        return {'code': 404, 'msg': 'User Not Found'}
    else:
        spring_courses = []
        summer_courses = []
        autumn_courses = []
        results = response['results']
        for course in results:
            if course['courseRoleId'] is 'Student':
                courses.append(course['courseId'])
    