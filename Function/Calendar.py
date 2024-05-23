import requests


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
    print(response.json())
    if response.json()['status'] == 401:
        return {'code': 401, 'msg': 'Unauthorized'}
    return response.json()['results']
