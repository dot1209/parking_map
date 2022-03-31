from pydantic import BaseModel

class Item(BaseModel):
    parking_info: Dict[str, str]

class Info(BaseModel):
    ID: str
    password: str
    verify: str
