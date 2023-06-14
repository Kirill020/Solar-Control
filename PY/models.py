from pydantic import BaseModel

class LoginModel(BaseModel):
    username: str
    password: str

class GroupDataModel(BaseModel):
    id: int
    performance: float
    voltage: float
    power: float