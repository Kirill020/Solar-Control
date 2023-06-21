from fastapi import FastAPI
import jwt
from db_handler import SqliteDB
from models import LoginModel, GroupDataModel, AuthModel, RegModel, VerifyEmailModel
from typing import Union
from datetime import datetime, timedelta
import os
import json
import random
import smtplib
import time

security_code = None
secret_key = "TOKEN_KEY"
app = FastAPI(title="SolarControl API", version="0.2.0", description="API for SolarControl project")

#authenticate user
@app.post("/auth", tags=["auth"])
async def login(login_data: Union[LoginModel, AuthModel]):
    if isinstance(login_data, LoginModel):
        password, login = login_data.password, login_data.login
        result = SqliteDB.authenticate_user(login, password)
        if result[0]:
            token = create_token(result[1])
            return {"token": token}
    else:
        token = login_data.token
        if token is not None:
            ver = verify_token(token)
            if ver == True:
                return True
            else:
                return False, ver
    return False

#register user 
@app.post("/reg", tags=["reg"])
async def registration(reg_data: RegModel):
    if not all(reg_data.dict().values()):
        return False
    else:
        login = reg_data.login, password = reg_data.password, username = reg_data.username, adress = reg_data.adress, code = reg_data.code
        if SqliteDB.get_user_data(login,None) is None:
            if code == security_code["code"] and (time.time() - security_code['timestamp']) < 180 and security_code['form_name'] == "Reg_form":
                                            #to do      ->        change path to default image on a server
                with open(r'Path\\to\\image\\file\\on\\server ', 'rb') as f:
                    image_binary = f.read()
                if SqliteDB.add_user(username, login,adress, password, image_binary):
                    return True, {"Info": "User has been succesfuly refistred"}
                else:
                    return False, {"Error": "Something went wrong"}
            else:
                return False, {"Error": "Invalid security code"}    
        else:
            return False, {"Error": "This user has been registered earlier"}
        

#verify email using security code
@app.post("/verify_email", tags=["verify email"])
async def verify_email(e_mail: VerifyEmailModel):
    if not all(e_mail.dict().values()):
        return False, {"Error": "Not enough data"}      
    else:
        global security_code    
        email, form_name = e_mail.login, e_mail.form_name
        user_data = SqliteDB.get_user_data(email,None)
        if form_name == "Reg_form" and user_data[0] is None and user_data[1] is None:
            security_code = generate_code(email, form_name)
            return True, {"Info": "Security code has been sendet"}
        elif form_name != "Reg_form" and user_data[0] is not None and user_data[1] is not None:
            security_code = generate_code(email, form_name)
            return True, {"Info": "Security code has been sendet"}                        
        else:
            return False, {"Error": "Input correct email please"}



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

#generate security code
def generate_code(email, form_name) -> int:
    try:
        code = int(random.randint(100000, 999999))

        #add this data to enviroment variable \/
        from_address = 'work.tanasiichuk@gmail.com'
        to_address = email
        subject = 'Security Code'
        body = f'Your security code is: {code}'
        message = f'Subject: {subject}\n\n{body}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, 'wilgfdzekbdoboxp')
        server.sendmail(from_address, to_address, message)
        server.quit()

        return {
        'code': code,
        'timestamp': time.time(),
        'form_name': form_name
        }
    except Exception as e:
        return{"Error", f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
