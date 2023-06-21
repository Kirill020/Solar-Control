from pydantic import BaseModel
from typing import Optional

class LoginModel(BaseModel):
    login: str
    password: str


class AuthModel(BaseModel):
    token: str

class VerifyEmailModel(BaseModel):
    login: str
    form_name: str

class RegModel(BaseModel):
    login: str
    password: str
    username: str
    adress: str
    code: int

class GroupDataModel(BaseModel):
    id: int
    performance: float
    voltage: float
    power: float