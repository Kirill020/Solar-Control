from pydantic import BaseModel
from typing import Optional

class LoginModel(BaseModel):
    login: str
    password: str

class AuthModel(BaseModel):
    token: str

class VerifyEmailModel(BaseModel):
    login: str

class VerifyNewEmailModel(BaseModel):
    old_login: str
    new_login: str
    token:str

class RegModel(BaseModel):
    login: str
    password: str
    username: str
    adress: str
    number: str
    code: int

class GroupDataModel(BaseModel):
    id: int
    performance: float
    voltage: float
    power: float

class ChangePassModel(BaseModel):
    code: int
    login: str
    username: str
    old_password: str
    new_password: str
    number: str

class ChangeNameModel(BaseModel):
    username: str
    token: str

class ChangeLoginModel(BaseModel):
    old_login: str
    new_login: str
    password: str
    code: int
    token:str

class ChangeAvatarModel(BaseModel):
    login: str
    avatar: str

class GetAllPanelsPerformanceModel(BaseModel):
    token: str
    
class GetIntervalPanelsPerformanceModel(BaseModel):
    token: str
    startdate: str
    enddate: Optional[str]
    panelgroup_id: int
#                       to do
#change phone number with verification