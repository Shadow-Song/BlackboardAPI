import requests


def login(account, password):
    url = 'https://bbh.yangyq.net/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    }

    body = {
        'username': account,
        'password': password
    }

    response = requests.post(url, headers=headers, verify=False, json=body)
    return response.json()
