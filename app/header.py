from pydantic import BaseModel

class Info(BaseModel):
    ID: str
    password: str
    verify: str
