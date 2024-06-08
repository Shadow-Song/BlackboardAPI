from fastapi import FastAPI
from Account import Login
from Blackboard import Course, UserID
from Security import Security

import Models

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/hello/{name}/')
async def say_hello(name: str):
    return {'message': f'Hello {name}'}


@app.post('/login')
async def login(body: Models.LoginRequest):
    # password_decrypted = Security.decrypt(password.encode())
    return Login.login(username=body.username, password=body.password)


@app.get('/logout')
async def logout(username: str):
    return Login.logout(username=Security.decrypt(username))


@app.get('/user_id')
async def get_user_id(username: str, session: str):
    return UserID.get_user_id(username=username, session=session)


@app.get('/user_name')
async def get_user_name(user_id: str, session: str):
    return UserID.get_user_name(user_id=user_id, session=session)


@app.get('/course_list')
async def get_course_list(user_id: str, session: str):
    return Course.get_course_list(user_id=user_id, session=session)

@app.get('/course_contents')
async def get_course_contents(course_id: str, session: str):
    return Course.get_course_contents(course_id=course_id, session=session)

@app.get('/course_info')
async def get_course_info(course_id: str, session: str):
    return Course.get_course_info(course_id=course_id, session=session)
