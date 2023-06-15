from pydantic import BaseModel
from typing import Optional

class LoginModel(BaseModel):
    username: str
    password: str


class AuthModel(BaseModel):
    token: str

class GroupDataModel(BaseModel):
    id: int
    performance: float
    voltage: float
    power: float