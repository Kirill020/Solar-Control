from fastapi import FastAPI, APIRouter
import jwt
from db_handler import SqliteDB
from models import LoginModel, GroupDataModel, AuthModel, RegModel, VerifyEmailModel,VerifyNewEmailModel, ChangePassModel, ChangeNameModel, ChangeLoginModel, GetAllPanelsPerformanceModel, GetIntervalPanelsPerformanceModel
from typing import Union
from datetime import datetime, timedelta
import os
import json
import random
import smtplib

#it`s gotta be as environment variable
secret_key = "TOKEN_KEY"
app = FastAPI(title="SolarControl API", version="0.2.0", description="API for SolarControl project")
updaterouter = APIRouter()
getrouter = APIRouter()


#authenticate user
@app.post("/auth", tags=["auth"])
async def login(login_data: Union[LoginModel, AuthModel]):
    if isinstance(login_data, LoginModel):
        password, login = login_data.password, login_data.login
        result = SqliteDB.authenticate_user(login, password)
        if result[0]:
            token = create_token(result[1])
            userdata = SqliteDB.get_user_data(None, result[1])
            del userdata["Person_id"]
            return {"token": token,
                    "userdata" : userdata}
    else:
        token = login_data.token
        if token is not None:
            ver = verify_token(token)
            if ver[0] == True:
                userdata = SqliteDB.get_user_data(None, ver[1]["Person_id"])
                del userdata["Person_id"]
                return {"userdata" : userdata}
            else:
                return False, ver
    return False

#register user 
@app.post("/reg", tags=["reg"])
async def registration(reg_data: RegModel):
    if not all(reg_data.dict().values()):
        return False
    else:
        login = reg_data.login, password = reg_data.password, username = reg_data.username, adress = reg_data.adress, number = reg_data.number, code = reg_data.code
        if SqliteDB.get_user_data(login,None)[0] is None:
            if verify_code(code, login):
                                            #to do      ->        change path to default image on a server
                with open(r'Path\\to\\image\\file\\on\\server ', 'rb') as f:
                    image_binary = f.read()
                if SqliteDB.add_user(username, login, adress, password, image_binary, number):
                    return True, {"Info": "User has been succesfuly registered"}
                else:
                    return False, {"Error": "Something went wrong"}
            else:
                return False, {"Error": "Invalid security code"}    
        else:
            return False, {"Error": "This user has been registered earlier"}
        

                                                    #update user data

#update password
@updaterouter.patch("/password", tags=["update password"])
async def change_pass(change_pass_data: ChangePassModel):
    if not all(change_pass_data.dict().values()):
        return False, {"Error": "Not enough data"}      
    else:
        code, login,username, old_password, new_password, number = change_pass_data.code, change_pass_data.login, change_pass_data.username, change_pass_data.old_password, change_pass_data.new_password, change_pass_data.number
        if old_password == "None":
            user_data = SqliteDB.get_user_data(login, None)
            
            if user_data[0] is not None and user_data[0]["U_name"] == username:# and user_data[0]["U_number"] == number:
                if verify_code(code, login):
                    if SqliteDB.update_user_data(user_data[0]["Person_id"], None, None, None, new_password, None, None):
                        return True, {"info": "password has been successfuly updated"}
                    else:
                        return False, {"error": "something went wrong"}
                else:
                    return False, {"error": "invalid security code"}
            else:
                return False, {"error": "user not found"}
        else:
            user_data = SqliteDB.authenticate_user(login, old_password)
            if user_data[0]:
                if verify_code(code, login):
                    if SqliteDB.update_user_data(user_data[1], None, None, None, new_password, None, None):
                        return True, {"info": "password has been successfuly updated"}
                    else:
                        return False, {"error": "something went wrong"}
                else:
                    return False, {"error": "invalid security code"}
            else:
                return False, {"error": "user not found"}


#update username
@updaterouter.patch("/username", tags=["update username"])
async def change_name(change_name_data: ChangeNameModel):
    if not all(change_name_data.dict().values()):
        return False, {"Error": "Not enough data"}      
    else:
        username, token = change_name_data.username, change_name_data.token
        if token is not None:
            ver = verify_token(token)
            if ver[0] == True:
                if SqliteDB.update_user_data(ver[1]["Person_id"], username, None, None, None, None, None):
                    return True
                else:
                    return False, {"error": "something went wrong"}
            else:
                return False, ver


#update email
@updaterouter.patch("/email", tags=["update email"])
async def change_email(change_email_data:ChangeLoginModel):
    if not all(change_email_data.dict().values()):
        return False, {"error": "Not enough data"}
    else:
        old_email, new_email, password, code, token = change_email_data.old_login, change_email_data.new_login, change_email_data.password, change_email_data.code, change_email_data.token
        ver = verify_token(token)
        if ver[0]:
            if verify_code(code, new_email):
                if ver[1]["Person_id"] == SqliteDB.authenticate_user(old_email,password)[1]:
                    if SqliteDB.update_user_data(ver[1]["Person_id"], None, new_email, None, None, None, None):
                        return True, {"info": "login has been successfuly updated"}
                    else:
                        return False, {"error": "something went wrong"}
                else:
                    return False, {"error": "invalid user"}
            else:
                return False, {"error": "invalid security code"}
        else:
            return False, ver


#verify email using security code
@app.post("/verify-email", tags=["verify email"])
async def verify_email(e_mail: Union[VerifyEmailModel, VerifyNewEmailModel]):
    if isinstance(e_mail, VerifyNewEmailModel):
        old_email, new_email, token = e_mail.old_login, e_mail.new_login, e_mail.token
        ver = verify_token(token)
        if ver[0]:
            userdata = SqliteDB.get_user_data(None, ver[1]["Person_id"])
            if userdata[0]["U_email"] == old_email:
                return generate_code(new_email)
            else:
                return False, {"error", "input valid email"}
        else:
            return False, ver
    else:
        email = e_mail.login
        return generate_code(email)
        


                                        #get data


#get all data about solar panels
@getrouter.post("/global-panels-performance", tags=["all panels performance"])
async def get_all_panels_performance(request_data: GetAllPanelsPerformanceModel):
    token = request_data.token
    ver = verify_token(token)
    if ver[0]:
        return SqliteDB.get_panel_group_data(ver[1]["Person_id"], None)
    else:
        return False, ver
    

#get interval data about solar panels
@getrouter.post("/interval-panels-performance", tags=["interval panels performance"])
async def get_interval_panels_performance(request_data: GetIntervalPanelsPerformanceModel):
    if request_data.token is None or request_data. startdate is None or request_data.panelgroup_id is None:
        return False, {"error": "Not enough data"}
    else:
        token, startdate, enddate, panelgroup_id = request_data.token, request_data.startdate, request_data.enddate, request_data.panelgroup_id
        ver = verify_token(token)
        if ver[0]:
            if enddate is None:
                return SqliteDB.get_interval_panel_group_data(ver[1]["Person_id"], panelgroup_id, datetime.strptime(startdate, "%Y-%m-%d-%H"), None)
            else:
                return SqliteDB.get_interval_panel_group_data(ver[1]["Person_id"], panelgroup_id, datetime.strptime(startdate, "%Y-%m-%d-%H"), datetime.strptime(enddate, "%Y-%m-%d-%H"))
        else:
            return False, ver


#add data from Arduino Uno WiFi Rev2
@app.post("/group-data", tags=["group data"])
async def add_group_data(group_data: GroupDataModel):
    if not all(group_data.dict().values()):
        id, performance, voltage, power = None, None, None, None
    else:
        id, performance, voltage, power = group_data.id, group_data.performance, group_data.voltage, group_data.power

        panels_data = SqliteDB.get_panel_group_data_api(id)

        if panels_data is not None:
            id_panel_group, panels_address = panels_data["Id_PanelGroup"], panels_data["Panels_adress"]
            SqliteDB.update_penels_performance(id, id_panel_group, performance, voltage, power, panels_address)
        else:
            #if in database doesn't exist data about some panels group save this data to add their in future
            new_group = {'id': id, 'performance': performance, 'voltage': voltage, 'power': power}
            add_new_data(new_group)
        
#add data about new solar panels group to buffer file (I have to change it and save data to special table in db until user add them)
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

#create token for next 24 hours
def create_token(person_id: int) -> str:
    expires = datetime.utcnow() + timedelta(hours=24)
    payload = {"person_id": person_id, "exp": expires}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

#verify token
def verify_token(token:str) -> bool:
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        if datetime.utcfromtimestamp(payload["exp"]) >=datetime.utcnow():
            return True, {"Person_id": payload["person_id"]}
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    return False

#generate security code
def generate_code(email):
    try:
        result = SqliteDB.get_code(email)
        if result[0]:
            return False, {"error": "too many attempts"}
        else:
            code = int(random.randint(100000, 999999))

            #add this data to environment variable \/ 
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

            SqliteDB.add_code(code, email)
            return True, {"info": "code has been sendet successfuly"}
        
    except Exception as e:
        return{"Error", f"An error occurred: {str(e)}"}

#verify security code
def verify_code(code, email):
    result = SqliteDB.get_code(email)
    if result[0] == True:
        if code == result[1][0][0]:
            SqliteDB.delete_code(code, email, result[1][0][1])
            return True
        else:
            return False
    else:
        return False
    
app.include_router(updaterouter, prefix="/update")
app.include_router(getrouter, prefix="/get")
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
    