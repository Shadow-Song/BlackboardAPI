import requests
import urllib3
from . import UserID

urllib3.disable_warnings()


# 获取某一用户的课程列表，返回课程ID、课程名称、课程时间（学期）
def get_course_list(user_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/users/{user_id}/courses'
    header = {
        'xweb_xhr': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': f's_session_id={session};'
    }
    response = requests.get(url, headers=header, verify=False).json()
    if 'status' in response:
        if response['status'] == 401:
            return {'code': 401, 'msg': 'Unauthorized'}
        elif response['status'] == 404:
            return {'code': 404, 'msg': 'User Not Found'}

    courses = []
    results = response['results']
    for course in results:
        # 只获取作为学生的课程（暂不支持教师和助教）
        if course['courseRoleId'] == 'Student':
            course_id = course['courseId']
            # 根据课程ID获取课程名称和时间
            course_info = get_course_info(course_id, session)
            print(course_info)
            # if 'code' in course_info:
            #     return course_info
            courses.append(course_id)

    return {'code': 200, 'courses': courses}


# 获取某一课程的信息，返回课程ID、课程名称、课程时间（学期）
def get_course_info(course_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{course_id}'
    header = {
        'xweb_xhr': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': f's_session_id={session};'
    }
    response = requests.get(url, headers=header, verify=False).json()
    if 'status' in response:
        if response['status'] == 401:
            return {'code': 401, 'msg': 'Unauthorized'}
        elif response['status'] == 404:
            return {'code': 404, 'msg': 'User Not Found'}
    course_name = response['name']
    course_id_long = response['courseId']

    course_year = course_id_long[0:4]
    course_season = course_id_long[4]

    # 根据字符替换学期
    if course_season == 'C':
        course_season = '春'
    elif course_season == 'X':
        course_season = '夏'
    elif course_season == 'Q':
        course_season = '秋'

    return {'course_id': course_id, 'course_name': course_name, 'course_time': f'{course_year}{course_season}'}


def get_course_contents(course_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{course_id}/contents'
    header = {
        'xweb_xhr': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': f's_session_id={session};'
    }
    response = requests.get(url, headers=header, verify=False).json()
    if 'status' in response:
        if response['status'] == 401:
            return {'code': 401, 'msg': 'Unauthorized'}
        elif response['status'] == 404:
            return {'code': 404, 'msg': 'User Not Found'}

    print(response)
    contents_list = []
    results = response['results']
    for result in results:
        if result['availability']['available'] == 'Yes':
            info = {'id': result['id'], 'title': result['title'], 'hasChildren': result['hasChildren']}
            contents_list.append(info)

    return {'code': 200, 'contents': contents_list}


def get_course_content_info(course_id: str, content_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{course_id}/contents/{content_id}'
    header = {
        'xweb_xhr': '1',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Content-Type': 'application/json',
        'Cookie': f's_session_id={session};'
    }
    response = requests.get(url, headers=header, verify=False).json()
    if 'status' in response:
        if response['status'] == 401:
            return {'code': 401, 'msg': 'Unauthorized'}
        elif response['status'] == 404:
            return {'code': 404, 'msg': 'User Not Found'}

    children = []
    results = response['results']
    for result in results:
        if (result['availability']['available'] == 'Yes' and
                result['contentHandler']['id'] == 'resource/x-bb-assignment'):
            info = {
                'id': result['id'],
                'parentID': result['parentId'],
                'title': result['title'],
                'body': result['body'],
                'position': result['position'],
            }
            children.append(info)
    return {'code': 200, 'children': children}


