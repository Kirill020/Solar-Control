# import fasapi
from fastapi import FastAPI, HTTPException

# import db handler
from db_handler import SqliteDB

# import models
from models import CheckModel, GroupDataModel

# import requests for weather api
import requests

# import datetime for weather api
from datetime import datetime

import os
import json

app = FastAPI(title="SolarControl API", version="0.1.0", description="API for SolarControl project")

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.post("/check")
async def auth(auth_data: CheckModel):
    if not all(auth_data.dict().values()):
        raise HTTPException(status_code=400, detail="Missing required fields in JSON")
    password = auth_data.password
    username = auth_data.username
    print(username)
    print(password)


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


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
