import requests
import urllib3
import UserID


urllib3.disable_warnings()


def get_course_info(course_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{course_id}'
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
        return {'code': 404, 'msg': 'Course Not Found'}
    course_name = response['name']

    url_2 = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{course_id}/users'
    response_2 = requests.get(url_2, headers=header, verify=False).json()
    if response_2['status'] == 401:
        return {'code': 401, 'msg': 'Unauthorized'}
    elif response_2['status'] == 404:
        return {'code': 404, 'msg': 'Course Not Found'}
    results = response_2['results']
    teacher_name = 'Unknown'
    teacher_college = 'Unknown'
    for result in results:
        if result['role'] == 'Instructor':
            teacher_id = result['userId']
            teacher_info = UserID.get_user_name(teacher_id, session)
            if teacher_info['code'] == 200:
                teacher_name = teacher_info['name']
                teacher_college = teacher_info['college']
            break
    return {'code': 200, 'course_name': course_name, 'teacher_name': teacher_name, 'teacher_college': teacher_college}
        
    
def get_course_contents(course_id: str, session: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{course_id}/contents'
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
        return {'code': 404, 'msg': 'Course Not Found'}
    
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
        return {'code': 404, 'msg': 'Course Not Found'}
    
    children = []
    results = response['results']
    for result in results:
        if result['availability']['available'] == 'Yes' and result['contentHandler']['id'] == "resource/x-bb-assignment":
            info = {
                'id': result['id'], 
                'parentID': result['parentId'],
                'title': result['title'], 
                'body': result['body'], 
                'position': result['position'],
            }
            children.append(info)

