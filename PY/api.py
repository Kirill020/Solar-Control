# import fasapi
from fastapi import FastAPI, HTTPException

# import jwt tokens
import jwt

# import db handler
from db_handler import SqliteDB

# import models
from models import LoginModel, GroupDataModel

# import requests for weather api
import requests

# import datetime for weather api
from datetime import datetime, timedelta

import os
import json

secret_key = os.environ.get("TOKEN_KEY")
app = FastAPI(title="SolarControl API", version="0.1.0", description="API for SolarControl project")

@app.get("/")
async def index():
    return {"message": "Hello World"}



@app.post("/login")
async def login(login_data: LoginModel):
    if not all(login_data.dict().values()):
        raise HTTPException(status_code=400, detail="Missing required fields in JSON")
    password = login_data.password
    username = login_data.username
    result = SqliteDB.authenticate_user(username, password)
    if result[0]:
        token = create_token(result[1])
        return{"token": token}



#get data from Arduino Uno WiFi Rev2
@app.post("/group_data")
async def add_group_data(group_data: GroupDataModel):
    if not all(group_data.dict().values()):
        id = None
        performance = None
        voltage = None
        power = None
    else:
        id = group_data.id
        performance = group_data.performance
        voltage = group_data.voltage
        power = group_data.power

        Panels_Data = SqliteDB.get_panel_group_data_api(id)

        if Panels_Data is not None:
            Id_PanelGroup = Panels_Data["Id_PanelGroup"]
            Person_id = Panels_Data["Person_id"]
            Panels_amount = Panels_Data["Panels_amount"]
            Panels_adress = Panels_Data["Panels_adress"]
            SqliteDB.update_penels_group(Id_PanelGroup, Person_id, Panels_amount, Panels_adress, performance, voltage, power, id)
        else:
            #if in database does`t exist data about some panels group save this data to add their in future
            new_group = {}
            new_group['id'] =  id
            new_group['performance'] =  performance
            new_group['voltage'] =  voltage
            new_group['power'] =  power

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
        pass
    except jwt.InvalidTokenError:
        pass
    return False



if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
