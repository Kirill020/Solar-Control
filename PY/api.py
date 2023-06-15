from fastapi import FastAPI
import jwt
from db_handler import SqliteDB
from models import LoginModel, GroupDataModel, AuthModel
from typing import Union
from datetime import datetime, timedelta
import os
import json

secret_key = "TOKEN_KEY"
app = FastAPI(title="SolarControl API", version="0.2.0", description="API for SolarControl project")


@app.post("/auth", tags=["auth"])
async def login(login_data: Union[LoginModel, AuthModel]):
    if isinstance(login_data, LoginModel):
        password, username = login_data.password, login_data.username
        result = SqliteDB.authenticate_user(username, password)
        if result[0]:
            token = create_token(result[1])
            return {"token": token}
    else:
        token = login_data.token
        if token is not None and verify_token(token):
            return True
    return False

#get data from Arduino Uno WiFi Rev2
@app.post("/group_data", tags=["group_data"])
async def add_group_data(group_data: GroupDataModel):
    if not all(group_data.dict().values()):
        id, performance, voltage, power = None, None, None, None
    else:
        id, performance, voltage, power = group_data.id, group_data.performance, group_data.voltage, group_data.power

        panels_data = SqliteDB.get_panel_group_data_api(id)

        if panels_data is not None:
            id_panel_group, person_id, panels_amount, panels_address = panels_data["Id_PanelGroup"], panels_data["Person_id"], panels_data["Panels_amount"], panels_data["Panels_adress"]
            SqliteDB.update_penels_group(id_panel_group, person_id, panels_amount, panels_address, performance, voltage, power, id)
        else:
            #if in database doesn't exist data about some panels group save this data to add their in future
            new_group = {'id': id, 'performance': performance, 'voltage': voltage, 'power': power}
            add_new_data(new_group)
        

def add_new_data(new_group):
    file_path = 'new_group.txt'
    if os.path.isfile(file_path) and os.stat(file_path).st_size != 0:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.append(new_group)

    with open(file_path, 'w') as file:
        json.dump(existing_data, file)


def create_token(person_id: int) -> str:
    expires = datetime.utcnow() + timedelta(hours=24)
    payload = {"person_id": person_id, "exp": expires}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

def verify_token(token:str) -> bool:
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        if datetime.utcfromtimestamp(payload["exp"]) >=datetime.utcnow():
            return True
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    return False



if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
