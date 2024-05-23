from pydantic import BaseModel


class CalendarResponse(BaseModel):
    result: list


class CalendarRequest(BaseModel):
    s_session_id: str
