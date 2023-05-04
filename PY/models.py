from pydantic import BaseModel

class CheckModel(BaseModel):
    username: str
    password: int

class GroupDataModel(BaseModel):
    id: int
    performance: float
    voltage: float
    power: float