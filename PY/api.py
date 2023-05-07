from fastapi import FastAPI

# import db handlers
from db_handler import SqliteDB

# import models
from models import CheckModel, GroupDataModel

import requests

from datetime import datetime

app = FastAPI(title="SolarControl API", version="0.1.0", description="API for SolarControl project")

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.post("/check")
async def auth(auth_data: CheckModel):
    password = auth_data.password
    username = auth_data.username
    print(username)
    print(password)

@app.post("/group_data")
async def add_group_data(group_data: GroupDataModel):
    id = group_data.id
    performance = group_data.performance
    voltage = group_data.voltage
    power = group_data.power
    Panels_Data = SqliteDB.get_panel_group_data_api(id)
    if(Panels_Data is not None):
        Id_PanelGroup = Panels_Data["Id_PanelGroup"]
        Person_id = Panels_Data["Person_id"]
        Panels_amount = Panels_Data["Panels_amount"]
        Panels_adress = Panels_Data["Panels_adress"]
        SqliteDB.update_penels_group(Id_PanelGroup, Person_id, Panels_amount, Panels_adress, performance, voltage, power, id)
        get_weather_from_api(Panels_adress, Id_PanelGroup)




def get_weather_from_api(location: str, Id_PanelGroup: int):
    api_key = 'e48976283ebb45a7ae1102438231003'
    date = datetime.today().strftime('%Y-%m-%d')
    hour = datetime.now().hour  

    url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={date}&hour={hour}"
    response = requests.get(url)
    data = response.json()

    temperature = data['forecast']['forecastday'][0]['hour'][0]['temp_c']
    wind_speed = data['forecast']['forecastday'][0]['hour'][0]['wind_kph']
    weather_type = data['forecast']['forecastday'][0]['hour'][0]['condition']['text']

    SqliteDB.update_weather(Id_PanelGroup, weather_type, temperature, wind_speed)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
    