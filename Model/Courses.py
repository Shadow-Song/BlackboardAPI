from pydantic import BaseModel


class Course(BaseModel):
    id: str
    userId: str
    courseId: str
    dataSourceId: str
    created: str
    modified: str
    availability: dict
    courseRoleId: str
    lastAccessed: str


