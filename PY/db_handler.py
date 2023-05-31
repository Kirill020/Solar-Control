import sqlite3 as sql
import hashlib
from datetime import datetime
import requests

class SqliteDB:

    #authentication user
    @staticmethod
    def authenticate_user(login: str, password: str) -> tuple[bool, int]:
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        cursor.execute("SELECT P_pass, Person_id FROM Users WHERE P_email_adress = ?", (login,))
        result = cursor.fetchone()
        if result is None:
            conn.close()
            return False, None

        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if password_hash == result[0]:
            conn.close()
            return True, result[1]

        conn.close()
        return False, None


    #get user data
    @staticmethod
    def get_user_data(login: str, Person_id: int):
        conn = sql.connect("C:\Solar Control\Solar-Control\PY\Solar_panels.db")
        cursor = conn.cursor()
        
        if login is not None:
            cursor.execute("SELECT * FROM Users WHERE P_email_adress = ?", (login,))
            result = cursor.fetchone()

        elif Person_id is not None:
            cursor.execute("SELECT * FROM Users WHERE Person_id = ?", (Person_id,))
            result = cursor.fetchone()

        else: result = None
        conn.close()

        if result is None:    
            return None, None
        else:

            User_data = {}
            User_data = {'Person_id':result[0], 'P_name':result[1], 'P_email_adress':result[2], 'P_adress':result[3]}
            return User_data, result[5]


    #get wetaher data
    @staticmethod
    def get_weather(id_panel_group: int):
        conn = sql.connect("C:\Solar Control\Solar-Control\PY\Solar_panels.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Weather WHERE Id_PanelGroup = ?", (id_panel_group,))
        result = cursor.fetchall()
        conn.close()

        if result is None:
            return None
        else:
            return result
        
    
    #get panels group data
    @staticmethod
    def get_panel_group_data(person_id: int, id_panel_group: int, date: datetime):
        conn = sql.connect("C:\Solar Control\Solar-Control\PY\Solar_panels.db")
        cursor = conn.cursor()
        if person_id is not None and id_panel_group is not None and date is not None:
            cursor.execute("SELECT Id_PanelGroup, Panels_amount, Panels_adress, Performance, Voltage, Power, Date FROM Panels WHERE Id_PanelGroup = ? AND Person_id = ? AND Date = ?", (id_panel_group, person_id, date))
            result = cursor.fetchall()    
        elif id_panel_group is not None:
            cursor.execute("SELECT Id_PanelGroup, Panels_amount, Panels_adress, Performance, Voltage, Power, Date FROM Panels WHERE Id_PanelGroup = ? AND Person_id = ?", (id_panel_group, person_id,))
            result = cursor.fetchall()

        elif date is not None:
            cursor.execute("SELECT Id_PanelGroup, Panels_amount, Panels_adress, Performance, Voltage, Power, Date FROM Panels WHERE Date LIKE ? || '%' AND Person_id = ?", (date, person_id))
            result = cursor.fetchall()

        elif person_id is not None:
            cursor.execute("SELECT Id_PanelGroup, Panels_amount, Panels_adress, Performance, Voltage, Power, Date FROM Panels WHERE Person_id = ?", (person_id,))
            result = cursor.fetchall()

        else: result = None
        conn.close()
        
        if result is None or len(result) == 0:
            return None
        
        else:
            return result


    #get panels data for api
    @staticmethod
    def get_panel_group_data_api(control_id: int):
        conn = sql.connect("C:\Solar Control\Solar-Control\PY\Solar_panels.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Id_PanelGroup, Person_id, Panels_amount, Panels_adress FROM Panels WHERE Control_id = ?", (control_id,))
        
        result = cursor.fetchone()
        if result is None:
            conn.close()
            return None
        else:
            conn.close()
            Panels_Data = []
            Panels_Data = {'Id_PanelGroup': result[0], 'Person_id': result[1], 'Panels_amount': result[2], 'Panels_adress': result[3]}
            return Panels_Data
    
    #add user
    @staticmethod
    def add_user(p_name: str, p_email_adress: str, p_adress: str, password: str, image_binary: bytes) -> bool:
        conn = sql.connect("C:\Solar Control\Solar-Control\PY\Solar_panels.db")
        cursor = conn.cursor()
        p_pass  = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cursor.execute("INSERT INTO Users (P_name, P_email_adress, P_adress, P_pass, P_avatar) VALUES (?, ?, ?, ?, ?)", (p_name, p_email_adress, p_adress, p_pass, image_binary,))
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM Users WHERE P_name = ? AND P_email_adress = ? AND P_adress = ?  LIMIT 1", (p_name,p_email_adress, p_adress,))
        result = cursor.fetchone()
        conn.close()
        if result is not None:
            return True
        else:
            return False
    
    #add panel group
    @staticmethod
    def add_panels_group(person_id: int, panels_amount: int, panels_adress: str, performance: float, voltage: float, power: float, control_id: int):
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(Id_PanelGroup) FROM Panels")
        result = cursor.fetchone()
        Id_PanelGroup = result[0]+1

        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H')
        query = "INSERT INTO Panels (Id_PanelGroup, Person_id, Panels_amount, Panels_adress, Performance, Voltage, Power, Date, Control_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (Id_PanelGroup, person_id, panels_amount, panels_adress, performance, voltage, power, date_str, control_id)
        cursor.execute(query, values)
        conn.commit()
        conn.close()


        api_key = 'e48976283ebb45a7ae1102438231003'
        date_api = datetime.today().strftime('%Y-%m-%d')
        hour = datetime.now().hour  

        url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={panels_adress}&dt={date_api}&hour={hour}"
        response = requests.get(url)
        data = response.json()

        temperature = data['forecast']['forecastday'][0]['hour'][0]['temp_c']
        wind_speed = data['forecast']['forecastday'][0]['hour'][0]['wind_kph']
        weather_type = data['forecast']['forecastday'][0]['hour'][0]['condition']['text']

        SqliteDB.update_weather(Id_PanelGroup, weather_type, temperature, wind_speed)

    #add weather data
    @staticmethod
    def add_weather_data(id_panels_group: int, weather_type: str, temperature: float, wind_speed: float):
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H')
        query = "INSERT INTO Weather (Id_PanelGroup, Weather_type, Date, Temperature, Wind_speed) VALUES (?, ?, ?, ?, ?)"
        values = (id_panels_group, weather_type, date_str, temperature, wind_speed)
        cursor.execute(query, values)
        conn.commit()
        conn.close()


    #update user info
    @staticmethod
    def update_user_data(person_id: int, new_name: str, new_email_adress: str, new_adress: str, new_pass: str, new_avatar) -> bool:
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()

        if new_name is not None:
            query = "UPDATE Users SET P_name = ? WHERE Person_id = ?"
            cursor.execute(query, (new_name, person_id))
            conn.commit()

        if new_email_adress is not None:
            query = "UPDATE Users SET P_email_adress = ? WHERE Person_id = ?"
            cursor.execute(query, (new_email_adress, person_id))
            conn.commit()

        if new_adress is not None:
            query = "UPDATE Users SET P_adress = ? WHERE Person_id = ?"
            cursor.execute(query, (new_adress, person_id))
            conn.commit()

        if new_pass is not None:
            password_hash = hashlib.sha256(new_pass.encode('utf-8')).hexdigest()
            query = "UPDATE Users SET P_pass = ? WHERE Person_id = ?"
            cursor.execute(query, (password_hash, person_id))
            conn.commit()

        if new_avatar is not None:
            query = "UPDATE Users SET P_avatar = ? WHERE Person_id = ?"
            cursor.execute(query, (new_avatar, person_id))
            conn.commit()

        cursor.execute("SELECT COUNT(*) FROM Users WHERE Person_id = ? LIMIT 1", (person_id,))
        result = cursor.fetchone()
        conn.close()

        return result[0] == 1

        

    #update panels data
    @staticmethod
    def update_penels_group(panels_id: int, person_id: int, panels_amount: int, panels_adress: str, performance: float, voltage: float, power: float, control_id: int):
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H')
        query = "INSERT INTO Panels (Id_PanelGroup, Person_id, Panels_amount, Panels_adress, Performance, Voltage, Power, Date, Control_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (panels_id, person_id, panels_amount, panels_adress, performance, voltage, power, date_str, control_id)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    #update weather data
    @staticmethod
    def update_weather(id_panels_group: int, weather_type: str, temperature: float, wind_speed: float):
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H')
        query = "INSERT INTO Weather (Id_PanelGroup, Weather_type, Date, Temperature, Wind_speed) VALUES (?, ?, ?, ?, ?)"
        values = (id_panels_group, weather_type, date_str, temperature, wind_speed)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
    
    #delete user
    @staticmethod
    def delete_user(person_id: int) -> bool:
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        cursor.execute("SELECT P_name FROM Users WHERE Person_id = ?", (person_id,))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Users WHERE Person_id = ?", (person_id,))
            conn.commit()
            conn.close()
            return True
    

    #delete panels group
    @staticmethod
    def delete_panels(id_panel_group: int, person_id: int, date: datetime) -> bool:
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Panels WHERE Person_id = ? AND Id_PanelGroup = ? AND Date = ?", (person_id, id_panel_group, date,))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Panels WHERE Person_id = ? AND Id_PanelGroup = ? AND Date = ?", (person_id, id_panel_group, date))
            conn.commit()
            conn.close()
            return True
    
    #delete weather
    @staticmethod
    def delete_weather(id_panel_group: int, date: datetime) -> bool:
        conn = sql.connect('C:\Solar Control\Solar-Control\PY\Solar_panels.db')
        cursor = conn.cursor()
        date_str = date.strftime('%Y-%m-%d-%H')  
        cursor.execute("SELECT * FROM Weather WHERE Id_PanelGroup = ? AND Date = ?", (id_panel_group, date_str))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Weather WHERE Id_PanelGroup = ? AND Date = ?", (id_panel_group, date_str,))
            conn.commit()
            conn.close()
            return True