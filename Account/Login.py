import requests
import re
import logging
import urllib3

urllib3.disable_warnings()

logger = logging.getLogger("utils.scheduler")
last_execution = 'ff46c2af-1f91-4ec6-b4bc-629e71fb1085_ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5Ljk1QzRILWdzNTBfTnpJOE15cnpkTVJERURIbDJJb2NOQV9IUkV5SmJiQW1OR08wYXlXZTRmcEY2bUt4c2tiTGNqYWdRaFRsYXluMjBLeDE3TlVobEVOMzE1VUhEYks3UW5IY2NUVHVEWTdGMG5abWxvRS1hcFVqX3VqZTNIcnFUbGRJUm9ZRG40ZVplVFZWLUhKWmFJVHpNOXlPRkRwc3dYVE9Qc2JRTmpRU25XalJJLTE0VFNCQjUxQ1VsS1psOGNXWUE2NVFGalJFWkFWS3RWMV9lUFRRTXNJaEUtaEV5TWJNXzZCbnBKcEw3bTdqWlJ2LTJ0MmJESUxkaVZ6U2NLZ2h0TWNHTzN5dGhLZnoyYWdLeXJaVU5XdDBVbDZRemVodElkSWZjTGg2c2pweHdJOFV6TFlSN0pURWxSMUhieVRpejBIb3JIdllHNHYxSTdSajZXOUZiQW5wSjZnV3lnTW1zX0pNOFZ6N3J1MmducnB1ZXBZMWt1djh1ZG15NzNZcEZFTFJnd3BDMW92V3VYNm1sS1FORmpkTGFEaEliLXBaMTNPTVlHRER5NGhOaHFVcXh5Wkt4ZnNvMUR0VEFiS3V2YVJsOXFSbjRGNk8zUWNYc1hraFZkMW1nOUg1M0tBNF9jQWZ6eUN3ZXFLX1JzNFdobGVmQ09SWVdlQjg2LU9lc0lJRlJzXzEzV2p4X05XeFY2MS1SeFJ4UzBGQ0RkUGpsdmRmamFUUXRnZURZZFBjdFhGRG1DbW1qbWJTUTRodHp6QUJCeDRENUF5RHRJT1NQMFduX21HMHVzYzdkcjJjS0Q3aFAwd2FpMWRGVEpmTXhOeVhxdTlnTjI2c2E1QnF1NEY0QXk3QU9IM05rZWFNZVpheWdob3YxV3IzemZobldjVTB3VE42OGc5dldCSXpUd28zY0ZVTE5fUU5KazdrekZOSS0yOFRwakRZYmFaSmwyNzNYeXduRkxNcTl5QTVfWTYwcXhEQk1HMG90cW1qTWlFS2pYV3AzVjRLSUROZHlYTlJTY09ucmU1OUR6eHA3ZkNyYVlUb0Znc2lueHdXM3ZvOE9RbzBoOTZueXNfbGdsU3JIMVZWcUhWNzV3T0dsRTRZd1BhN0F1Mk9qckhWeEkxdUtMb0lXYVJnT25pRHFRMVRuRUF1VjRROVhKdUZvRGNSQW8tN09WcWlxakZDejFFNy12QnByQ3NYMW5lNHF1am83QVUtX0ZGa1RhaW9GSWdmMTZsMXQ4NDhKRmlWd2VtMVNUOEFlcTZWN0VaVC1ZY0ZaNi1zMWFhX2lGV0tNMjVTOHVQTk9vOTVGU1BWYUdpbkhNYnF2Rmt2X29adXcycHJNTFhhUEl2OWhlRzZIVFJiekp2OEVKTDFMNGJjeDRIWjdqSGtIdVFoYTFLZXZxUzlQYnZFdHZDc3pVbFpMQUFOYXNzcWpjSmhZX3M3XzBja3VEazNSNUJ4S05zMTZXRlBHNERQeEY1MndxYVBrUkdpMHBrckNzdFJ5MmVkUEp1c1c5R2c2TENnVndqSTNmMTgyQVlXdTRxOFMzaS1tTzNsSTNxMld1UlVTWFNvcVNPbVVESVdKTlJmN2VvUDh1eGE1Z0JLcmdtNFc3a2Vva3dHYU1jVUV0QmlUY2cxeEVCTlBRQ0hmb1J5bU5KQ2NwMWEzVFJNaUtvUmxLQU1tZG10amZ5MWtiWVk5TTk0Q0RwVjFDdHYydDJOYzJVQ2NCZENlU2IxREMtWklrbXlGMU9lbDhneE8wSVlzbThnYUpoRmR3bU1xaFJYR3pvekIzbDZSNnhfMmFndWlrT2sweGdKNVlmS0FNWHVEU1ZnMGJYbHFjUmJvY3cwYV9ESFh4QUlwczQ1am9SMzV1ZHlIQjlMQ0s2ZzV2X1I4OGxfYUI2VlFoNHJXX3I4cmNZVXZYekxxNzFUUzRibS03NjFycW9xQ1plY2xsN0pLOFVOd3BOZGZybWJYRHZRZmlNY0JFaDREbW4yUTVuWFJMVzRaLWVQZjV6c2JGTjVLNktWRUQyVUQwaXdxU3JiQU1zUkNHRWFVZl8wX3NoMDNhZERDVno1c2IzU004N3FVcWJjb01EZ0QzbTVXQWlqNGVTNXFVMkc1S3dmcmJqX3RKbWtTWXZpSHQ5a1pTOHBGZEU4MGhiNVhReUZXUWVtUDdHTHhLS2Nkdko3OV9SQ1Btdk9UQXZPT1lUWi1kb1FzSF9INTVTZUJvbGZwS0tNMm5UMDZqbU01bnNfU1JwMHZZeVhqS1hoWWVpUUJyaUxpZlFKTHBSZmpRZW05STB0T3BKOVYySnhiZHpwZ0lFTlFNY3NMWWpxLU1wbkREQ1JNbnRUVTdHUVR2bWpWTHVPQk1jM3l5eGdxcVB3c3hXRVI2Q2lRVGYwQkNzMlFwbTZ6RE00ZEQ3UDZRakdyNjlhZnhZRzMyVENINnhUMC1OVl8xVnAxXzFBNDM1ZDNnXzdnXzBNVXFNaVNVcF9uV3QtQ0hMMzVqS0I4Q0xpWWNRc0gxem9uSUcyZ0IyUy1zajFGcGs1TExhSkkxLUY3RF9oZkRuWmtwZlBKRXpENkt6aFF2UHk0Zmc2SUNsRDBXMWR3cnNMelhlYmhpWXJ4cWE4ZUlDYjBNeTNoN0RBc0NNRmx6cUc1elpLcXV5QWFIc1BfWmtBbGFZcUpiUVFtaU12al8yMzF3Sk9IRkJCeVdQaXNQQ3I3MjR6eTBmUlpVUjRsZVpHdmRzOVdpOUxNYlVxbHBhWmNvME9oWTM1cFJRa2pWWXNqSW5Xc0JRUVN6OFNkd1VlMnNIVVNkRVY0Z21qS1E0OEFCY0dXRVZiM2Q5eHMyRHRwdG5CM21PTXZYWXNzOWVPc3lMMkM5OTV0UmpGLWZ0eWFjSHFEbVBrOFJBS2RoamlrU0dYcWJVaEdmSkRTSkZIMEc0NmRzZ0JsTHp5cjVRdk9icEpNTWl6UUpuY2JfRzQ3MXlDYTlxT3FCQmZxNGZLVFNmN3Z5QTVCcDRuRHJ4N0NNd00zQkhNSW5OZklqNzJoU0xRbFB0SGVJY2VrMzZOTjN3aFkyYXJ4ejBNZktCa2Nja0l2cjZDWFFqYklwV0JHaTJyWHRVOWJVVWhBRGtxMWJILWNraGRZRUxzeTVRZWdXVjJycy1hblpHR0tpNjZ0QkZpcEUzcVo5azh1a1VCMHVwYVJVdEd5WFNsQmotUWkxLXRMb3I2LWhuV2hEVXl3RHZYTVJ2cjhaN1J0ajEyaUZwT3dfMWFzbjFCbjFSMGMxTGc2TkJTZVdvLUhBa1dZd0FpZGJzYWluMUczME5YVlRVeG43UG1OazEzWjhyTHlrVkhrMlptbDlJQVd1blpWcjNYT1p2Q2RhWFFmRnVadE92dmlfQmtxRnZTckJxR2FUb3oyLU1hY3pFMzBremdTTzd1aFlmZnl6QnpRYU12YUpUSGZ0YlNwT0NqVVU2aEJ2TVVZdEV2Yjd1QWF2ejlOcnBlOWtoM2g1eGl5Rld0SG00M0k2eVlMeDFqWklNQmVMTW52R1V1YU1obEV0TDYyUkR4X0w0SmJmRTJwYjVrNXBOeF9CWC1mNVVZRWZSblZJVkxwQnUwV2Rib3FMbnNHcnJiU3FEaFJqMEpub1Q5WTQweTgzdzVKb2FOaXYzUEo0TmcxY0gtQ3ZwQ2FVaTVXUDZpUFpiX0xoZ29Pd0oteFZsMkxCenBRQ2FyX2lZX29YV1ZNUGswX0g5N0hKU3BCTDFpOTdCRTNpcTViblNUdzVDcjRKTWhFeU1OdFNwdkM2bFlKY3ZpeDBMVUxxckU0dmlYV2pDSEktT3NYaUFXdzVOSS1aMmZxb0p0cENySldMYlZ6QUlmREJXbzNjb3JIYi1mZG56c2FucVFCeUVFcUxpenVwYmU3ZlZYNldSNDdoOFd6VFNGOUVKVmhLVWlkcGVYeFZzNXRPODlGVHJNcG9UU1ZNc0g3WkdCUm9wcVE3YTB2aHdhWVZfa1NuaGY3alhiak42NmtIOGNEaHpRVFV6akRleGl0VUtuU2ZiMlpNR0ltV2JDcDNMdmlqbU1wM2hJdWNSY0JSY0VZU0VyU2hhQVZCNlNfNXJocldPcVRtZDBWZnJ4X3dOYnZ4TnNVcVlDNC1FSHU5dVBNWGFrcTZ2WktNZjJpV1JvVzRjT19aMG1sbjM2SGNGQ3R2OXpxZUVibmx4cU92OXlvcERVRW5id0lKZkpvdVh6SC1BcXpHLUpwWjdVLXhzNmYxa2NSMDNyTnJvLUlOckFKNl96VVBRNVBYZDI3cnNWVWtnVlJQc1dyZmVNTDY3QnBHX1c1TVNUZ3drRHNRME9EU2FJUG9mcUVJRV9xSjNrc3draVN6RUdvbXh5VmM1RV9QalhJcUJGbHFnT2V4bnprazBRVklucFFBZmRxdnpEVDJhQTFCY2JjZjI5R1lDRkY5LUk3Z3dIY3pSZElvb1lZQnk1YmJrNy00aU9xTGZXTkFjWmg2X05Fd0pkdC04Rk5KcGNhUERGMXZfSk0ydjUtRjVJWTJsa1RnSEkxRGdPaURkbVhaR0U4ZWNIdlZLcnViLUNKcklfbFFCWmNUV29JdWVnLXhXVGtYNDdaYVZxc2Z3OFNCX282T2dfNzZQUnI0WUZFbDE4YzlNSlI4dVZsN3FYcmhycnZEekt6d2xuS3VGOVhSU2dNckhmYzJqeW5ERThPeXVlQVR5V1JLcXg1U1MwY2RBVVZXR0RpY3M3eUE4TXJfRk1ma3F6bkx5SW1fRnlLYkp5LWFRNm53b1lIaUk2Y1VaOG9XRmtHVTlEZTlhRWlDUUUwcDQ5ZmpGN0xqME5rVVRXTVJtSEZGRlZGdlZBU1VrbzRmNXdKaVlzMEFnTkVTdFlITndHWjg2VnlVUEZoUmhneUN3aU9ncjIySUFGMFdocm4yNlphWU8zZkM2U1dDOEZNdnNxVDJscDRPVTl5UlV6bHZra1BfUllLenVlYmxKNWJ2OEMyZnFITW12Z25nYmdjVllfeWNMQjF5eTNZNmU3NFpiTlRzbFlqQXVVQjJMdGVPUTlqekNGUUtJYUZsZU9iaXltSEk1dGRHUHlrbWtSZWN3djdEQjRJSExnR1BBTlR0SzMyRnAtQ2RRc0dwVk8wLm1HWDVRX0UtYXlTSHFxLWR3ZEhCR0FsWHhQQUpEVnY3NUk2emhfanctLWdzQ1FzWXFDZ3BsYS11NGFzZGhrQ3Q4eHMxRW1YZ0h6aXJoNUdaMDBWcWVn'


def check_password(username, password):
    url = 'https://id.ouc.edu.cn/baseLogin/postLogin'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    }
    response = requests.post(url, headers=headers, verify=False, json={
        'account': username,
        'password': password,
        'randomCode': 'comsys-base-login',
        'isRememberPwdOpen': 0,
        'scale': 1
    })
    try:
        response = response.json()
    except:
        return False
    if response['code'] == 200:
        return True
    return False


def get_bb_token(username):
    global last_execution
    url = 'https://id.ouc.edu.cn/sso/login?service=https://wlkc.ouc.edu.cn/webapps/bb-sso-BBLEARN/index.jsp#/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    }
    content = requests.get(url, headers=headers, verify=False).text
    execution = re.search('<input type="hidden" name="execution" value="(.*?)"', content)

    try:
        if execution:
            execution = execution.group(1)
            last_execution = execution
        else:
            import uuid
            execution = str(uuid.uuid4())[:23] + last_execution[23:]
        url = 'https://id.ouc.edu.cn/sso/login'
        content = requests.post(url, headers=headers, data={
            'execution': execution,
            '_eventId': 'submit',
            'geolocation': '',
            'username': username,
            'password': '00001101',  # 随机？
            'service': 'https://wlkc.ouc.edu.cn/webapps/bb-sso-BBLEARN/index.jsp#/'
        }, verify=False).text
        token = re.search('<input type="hidden" value="(.*?)" name="token"/>', content)
        return token.group(1)
    except Exception as e:
        logger.error(f"get {username}'s token failed , error message:{e}")
        return None


def get_session_id(username, token=None):
    if not token:
        token = get_bb_token(username)
    for _ in range(2):
        try:
            url = 'https://wlkc.ouc.edu.cn/webapps/bb-sso-BBLEARN/execute/authValidate/customLogin'
            rep = requests.request(method="POST", url=url, data={"username": username, "token": token}, headers={
                'Connection': 'close',
            }, verify=False)
            s_session_id = rep.cookies.get('s_session_id', domain='wlkc.ouc.edu.cn', path='/')
            return f's_session_id={s_session_id};'
        except Exception as _:
            # 处理token变化的情况
            token = get_bb_token(username)
    return f's_session_id=None;'


def get_user_id(account: str, s_session_id: str):
    url = f'https://wlkc.ouc.edu.cn/learn/api/public/v1/users?userName={account}'
    headers = {
        'Cookie': f's_session_id={s_session_id};',
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
    print(response)
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


if __name__ == '__main__':
    num = '21020036048'
    passwd = ('Qx3MpbdKkm+3c7Y9fjXRLr2aAvt+s0dRFc57QFs5oUhBqBpEykSCf+B1Vm+'
              'qdlMs70P293L8Ic1DLQdxYlNOw23N68intO8bEJEo1lJOXv3/JrlQuqxWy+'
              'clYqd+XB5oLdKJspErstHH5trPQX6JhxdQWP51WgIhZszms6kgDGQ=')
    print(check_password(num, passwd))
    bb_token = get_bb_token(num)
    session_id = get_session_id(num, bb_token)
    print(session_id)
    user_id = get_user_id(num, session_id)
    print(user_id)
