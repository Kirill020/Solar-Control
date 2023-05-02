from fastapi import FastAPI

# import db handlers
from db_handler import SqliteDB

# import models
from models import AuthModel

app = FastAPI(title="SolarControl API", version="0.1.0", description="API for SolarControl project")

@app.get("/", tags=["Example route"])
async def index():
    return {"message": "Hello World"}

@app.post("/auth", tags=["Example route"])
async def auth(auth_data: AuthModel):
    password = auth_data.password
    username = auth_data.username
    print(username)
    print(password)

@app.get("/weather/{id}", tags=["Example route"])
async def weather(id: int):
    return {"message": "weather for {id}"}

@app.put("/weather/{id}", tags=["Example route"])
async def weather(id: int, data: dict):
    return {"message": "weather for {id}"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
    