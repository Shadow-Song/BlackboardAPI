from fastapi import FastAPI
from Application import Login, Models as LoginModel

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/hello/{name}/')
async def say_hello(name: str):
    return {'message': f'Hello {name}'}


@app.get('/get/query/')
async def get_query(a: str = None):
    return {'q': a}


@app.get('/get_calendar/')
async def get_calendar(session_id: str):
    response = Login.get_calendar(session_id)
    return response


@app.get('/get_user_id/')
async def get_course_list(account: str, session_id: str):
    response = Login.get_user_id(account=account, session_id=session_id)
    return response


@app.post('/post_login/')
async def post_login(request: LoginModel.LoginRequest):
    print('Logging in...')
    correct = Login.check_password(request.account, request.password)
    if correct:
        token = Login.get_bb_token(request.account)
        session_id = Login.get_session_id(request.account, token)
        user_id = Login.get_user_id(request.account, session_id)
        if user_id['code'] == 400:
            return {'code': 401, 'msg': 'Unauthorized'}
        return {'code': 200, 'msg': 'success', 'session_id': session_id}
    else:
        return {'code': 400, 'msg': 'Password Error'}


@app.post('/user_id')
async def get_user_id(request: LoginModel.UserIDRequest):
    response = Login.get_user_id(request.account, request.session_id)
    return response
