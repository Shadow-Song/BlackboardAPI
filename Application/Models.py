from pydantic import BaseModel


class LoginRequest(BaseModel):
    account: str = None
    password: str = None


class UserIDRequest(BaseModel):
    account: str = None
    session_id: str = None
