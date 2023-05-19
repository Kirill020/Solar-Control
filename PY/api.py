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

#data about new solar panels group(if exist)
new_group = {"id": None, "performance": None, "voltage": None, "power": None}

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

        if(Panels_Data is not None):
            Id_PanelGroup = Panels_Data["Id_PanelGroup"]
            Person_id = Panels_Data["Person_id"]
            Panels_amount = Panels_Data["Panels_amount"]
            Panels_adress = Panels_Data["Panels_adress"]
            SqliteDB.update_penels_group(Id_PanelGroup, Person_id, Panels_amount, Panels_adress, performance, voltage, power, id)
            get_weather_from_api(Panels_adress, Id_PanelGroup)
        else:
            #if in database does`t exist data about some panels group save this data to add their in future
            global new_group
            new_group['id'] =  id
            new_group['performance'] =  performance
            new_group['voltage'] =  voltage
            new_group['power'] =  power
        print(new_group["id"])
        




#get data about weather in solar panels group adress and add to database
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
