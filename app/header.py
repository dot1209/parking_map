from pydantic import BaseModel
import json

class Info(BaseModel):
    ID: str
    password: str
    verify: str

class personInfo(BaseModel):
    ID: str
    name: str
    dep: str
    tel: str
    email: str
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class motorInfo(BaseModel):
    ID: str
    brand: str
    color: str
    liClass: str
