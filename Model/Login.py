from pydantic import BaseModel


class LoginRequest(BaseModel):
    account: str = None
    password: str = None


class LoginResponse(BaseModel):
    code: int
    msg: str
    data: dict
