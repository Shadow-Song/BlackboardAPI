from fastapi import FastAPI
import Function.Account as Account
import Function.Calendar as Calendar
import Function.CourseList as CourseList
import Requests.Requests as Requests
from Model.Login import LoginRequest
import Database.Database as Database

app = FastAPI()
db = Database.init_database()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/hello/{name}/')
async def say_hello(name: str):
    return {'message': f'Hello {name}'}


@app.get('/get/query/')
async def get_query(a: str = None):
    return {'q': a}


# Login
@app.post('/post_login/')
async def post_login(user: LoginRequest):
    response = Account.login(user.account, user.password)
    if response.code == 200:
        if Database.add_account(
            account=user.account,
            password=user.password,
            db=db
        ):
            return response
        else:
            return {'code': 400, 'msg': 'Database Disconnections'}
    return {'code': 401, 'msg': response.msg}


@app.get('/logout/')
async def logout(account: str):
    if Database.delete_account(account=account, db=db):
        return {'code': 200, 'msg': 'Logged Out'}
    else:
        return {'code': 400, 'msg': 'Database Error'}

@app.get('/get_calendar/')
async def get_calendar(session_id: str):
    response = Calendar.get_calendar(session_id)
    return response


@app.get('/get_course_list/')
async def get_course_list(user_id: str, session_id: str):
    response = CourseList.get_course_list(user_id=user_id, s_session_id=session_id)
    return response

@app.get('/get_user_id/')
async def get_course_list(account: str, session_id: str):
    response = Requests.get_user_id(account=account, s_session_id=session_id)
    return response
