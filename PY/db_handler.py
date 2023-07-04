import sqlite3 as sql
from typing import Union
import hashlib
from datetime import datetime
import requests
import base64

class SqliteDB:

    #authentication user
    @staticmethod
    def authenticate_user(login: str, password: str) -> tuple[bool, Union[int, None]]:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT U_password, Person_id FROM Users WHERE U_email = ?", (login,))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False, None

        if password == result[0]:
            conn.close()
            return True, result[1]

        conn.close()
        return False, None


    #get user data
    @staticmethod
    def get_user_data(login: str, Person_id: int) -> Union[tuple, None]:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        
        if Person_id is None:
            cursor.execute("SELECT * FROM Users WHERE U_email = ?", (login,))
            result = cursor.fetchone()

        elif login is None:
            cursor.execute("SELECT * FROM Users WHERE Person_id = ?", (Person_id,))
            result = cursor.fetchone()

        else: result = None
        conn.close()

        if result is None:    
            return None
        else:
            encoded_photo = base64.b64encode(result[5]).decode('utf-8')
            User_data = {'Person_id':result[0], 'U_name':result[1], 'U_email':result[2], 'U_adress':result[3], 'U_number':result[6], "U_photo": encoded_photo}
            return User_data


    #get wetaher data
    @staticmethod
    def get_weather(perf_id: int, date: datetime) -> Union[list[tuple], None]:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()

        if perf_id is None:
            cursor.execute("SELECT * FROM Weather WHERE Date LIKE ?", (date + '%'))
            result = cursor.fetchall()
        elif date is None:
            cursor.execute("SELECT * FROM Weather WHERE Perf_id = ?", (perf_id,))
            result = cursor.fetchall()
        else:
            return None
        conn.close()

        if result is None:
            return None
        else:
            return result
        
    
    #get panels group data
    @staticmethod
    def get_panel_group_data(person_id: int, id_panel_group: int) -> Union[list[tuple], None]:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        if person_id is not None and id_panel_group is not None:
            query = """
                SELECT
                    Pan.Id_PanelGroup,
                    Pan.Panels_amount,
                    Pan.Panels_adress,
                    Pan.Control_id,
                    Perf.Performance,
                    Perf.Voltage,
                    Perf.Power,
                    Perf.Date,
                    Wea.Weather_type,
                    Wea.Temperature,
                    Wea.Wind_speed
                FROM
                    Panels AS Pan
                JOIN
                    Performance AS Perf ON Pan.Id_PanelGroup = Perf.Id_PanelGroup
                JOIN
                    Weather AS Wea ON Perf.Id = Wea.Perf_id
                WHERE
                    Pan.Person_id = ? AND Pan.Id_PanelGroup = ?
            """
            cursor.execute(query, (person_id, id_panel_group,))
            result = cursor.fetchall()    
        elif person_id is not None:
            query = """
                SELECT
                    Pan.Id_PanelGroup,
                    Pan.Panels_amount,
                    Pan.Panels_adress,
                    Pan.Control_id,
                    Perf.Performance,
                    Perf.Voltage,
                    Perf.Power,
                    Perf.Date,
                    Wea.Weather_type,
                    Wea.Temperature,
                    Wea.Wind_speed
                FROM
                    Panels AS Pan
                JOIN
                    Performance AS Perf ON Pan.Id_PanelGroup = Perf.Id_PanelGroup
                JOIN
                    Weather AS Wea ON Perf.Id = Wea.Perf_id
                WHERE
                    Pan.Person_id = ?
            """
            cursor.execute(query, (person_id,))
            result = cursor.fetchall()
        else: result = None
        conn.close()
        
        if result is None or len(result) == 0:
            return None
        else:
            return result


    #get interval panel`s group data
    @staticmethod
    def get_interval_panel_group_data(person_id: int, id_panel_group: int, start_date: datetime, end_date: datetime) -> Union[list[tuple], None]:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        #from start to now
        if start_date is not None and end_date is None:
            query = """
                SELECT
                    Pan.Id_PanelGroup,
                    Pan.Panels_amount,
                    Pan.Panels_adress,
                    Pan.Control_id,
                    Perf.Performance,
                    Perf.Voltage,
                    Perf.Power,
                    Perf.Date,
                    Wea.Weather_type,
                    Wea.Temperature,
                    Wea.Wind_speed
                FROM
                    Panels AS Pan
                JOIN
                    Performance AS Perf ON Pan.Id_PanelGroup = Perf.Id_PanelGroup
                JOIN
                    Weather AS Wea ON Perf.Id = Wea.Perf_id
                WHERE
                    Pan.Person_id = ? AND Pan.Id_PanelGroup = ? AND Perf.Date >= ? COLLATE BINARY
            """
            cursor.execute(query, (person_id, id_panel_group, start_date,))
            result = cursor.fetchall()    
        #from start to end
        elif start_date is not None and end_date is not None:
            query = """
                SELECT
                    Pan.Id_PanelGroup,
                    Pan.Panels_amount,
                    Pan.Panels_adress,
                    Pan.Control_id,
                    Perf.Performance,
                    Perf.Voltage,
                    Perf.Power,
                    Perf.Date,
                    Wea.Weather_type,
                    Wea.Temperature,
                    Wea.Wind_speed
                FROM
                    Panels AS Pan
                JOIN
                    Performance AS Perf ON Pan.Id_PanelGroup = Perf.Id_PanelGroup
                JOIN
                    Weather AS Wea ON Perf.Id = Wea.Perf_id
                WHERE
                    Pan.Person_id = ? AND Pan.Id_PanelGroup = ? AND Perf.Date >= ? AND Perf.Date <= ? COLLATE BINARY_NOCASE
            """
            cursor.execute(query, (person_id, id_panel_group, start_date, end_date,))
            result = cursor.fetchall()
        else: result = None
        conn.close()
        
        if result is None or len(result) == 0:
            return None
        else:
            return result


    #get panels data for api
    @staticmethod
    def get_panel_group_data_api(control_id: int) -> Union[tuple, None]:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Id_PanelGroup, Panels_adress FROM Panels WHERE Control_id = ?", (control_id,))
        
        result = cursor.fetchone()
        if result is None:
            conn.close()
            return None
        else:
            conn.close()
            Panels_Data = {'Id_PanelGroup': result[0], 'Panels_adress': result[1]}
            return Panels_Data
    

    #get code
    @staticmethod
    def get_code(email: str) -> tuple[bool, tuple]:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Code, Date FROM Codes WHERE Email = ?", (email,))

        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H-%M')
        date_now = datetime.strptime(date_str, '%Y-%m-%d-%H-%M')
        result = cursor.fetchall()
        flag = False
        valid_codes = []
        for i in range(len(result)):
            date_db = datetime.strptime(result[i][1], '%Y-%m-%d-%H-%M')
            time_difference = date_now - date_db
            if time_difference.total_seconds() > 120:   
                SqliteDB.delete_code(result[i][0],email, result[i][1])
            else:
                valid_codes.append(result[i])
                flag = True
        
        return flag, valid_codes


    #add user
    @staticmethod
    def add_user(u_name: str, u_email: str, u_adress: str, u_password: str, image_binary: bytes, u_number: str) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (U_name, U_email, U_adress, U_password, U_avatar, U_number) VALUES (?, ?, ?, ?, ?, ?)", (u_name, u_email, u_adress, u_password, image_binary, u_number,))
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM Users WHERE U_name = ? AND U_email = ? AND U_adress = ?  LIMIT 1", (u_name,u_email, u_adress,))
        result = cursor.fetchone()
        conn.close()
        if result is not None:
            return True
        else:
            return False
    
    #add panel group
    @staticmethod
    def add_panels_group(person_id: int, panels_amount: int, panels_adress: str, control_id: int) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        query = "INSERT INTO Panels (Person_id, Panels_amount, Panels_adress, Control_id) VALUES (?, ?, ?, ?)"
        values = (person_id, panels_amount, panels_adress, control_id)
        cursor.execute(query, values)
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM Panels WHERE Person_id = ? AND Panels_adress = ? AND Control_id = ?  LIMIT 1", (person_id,panels_adress, control_id,))
        result = cursor.fetchone()
        conn.close()
        if result is not None:
            return True
        else:
            return False

    #add weather data
    @staticmethod
    def add_weather_data(perf_id: int, weather_type: str, temperature: float, wind_speed: float) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H')
        query = "INSERT INTO Weather (Perf_id, Weather_type, Date, Temperature, Wind_speed) VALUES (?, ?, ?, ?, ?)"
        values = (perf_id, weather_type, date_str, temperature, wind_speed)
        cursor.execute(query, values)
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM Weather WHERE Perf_id = ? AND Date = ? LIMIT 1", (perf_id,date_str,))
        result = cursor.fetchone()
        conn.close()
        if result is not None:
            return True
        else:
            return False


    #add code
    @staticmethod
    def add_code(code: int, email: str) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()

        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H-%M')
        cursor.execute("INSERT INTO Codes (Email, Code, Date) VALUES (?, ?, ?)", (email, code, date_str,))
        conn.commit()

        cursor.execute("SELECT * FROM Codes WHERE Email = ? AND Code = ? AND Date = ? ", (email, code, date_str,))
        result = cursor.fetchone()
        conn.close()

        if result is not None:
            return True
        else:
            return False
        

    #update user info
    @staticmethod
    def update_user_data(user_id: int, new_name: str, new_email: str, new_adress: str, new_password: str, new_avatar, new_number: str) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()

        if new_name is not None:
            query = "UPDATE Users SET U_name = ? WHERE Person_id = ?"
            cursor.execute(query, (new_name, user_id))
            conn.commit()

        if new_email is not None:
            query = "UPDATE Users SET U_email = ? WHERE Person_id = ?"
            cursor.execute(query, (new_email, user_id))
            conn.commit()

        if new_adress is not None:
            query = "UPDATE Users SET U_adress = ? WHERE Person_id = ?"
            cursor.execute(query, (new_adress, user_id))
            conn.commit()

        if new_password is not None:

            #   we are getting alredy hash password    \/

            query = "UPDATE Users SET U_password = ? WHERE Person_id = ?"
            cursor.execute(query, (new_password, user_id))
            conn.commit()

        if new_avatar is not None:
            query = "UPDATE Users SET U_avatar = ? WHERE Person_id = ?"
            cursor.execute(query, (new_avatar, user_id))
            conn.commit()

        if new_number is not None:
            query = "UPDATE Users SET U_number = ? WHERE Person_id = ?"
            cursor.execute(query, (new_number, user_id))
            conn.commit()


        cursor.execute("SELECT COUNT(*) FROM Users WHERE Person_id = ? LIMIT 1", (user_id,))
        result = cursor.fetchone()
        conn.close()

        return result[0] == 1

        

    #update panels data
    @staticmethod
    def update_penels_performance(control_id: int, Id_PanelGroup: int, performance: float, voltage: float, power: float, panels_adress: str) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H')
        query = "INSERT INTO Performance (Control_id, Performance, Voltage, Power, Date, Id_PanelGroup) VALUES (?, ?, ?, ?, ?, ?)"
        values = (control_id, performance, voltage, power, date_str, Id_PanelGroup)
        cursor.execute(query, values)
        conn.commit()
        
        cursor.execute("SELECT MAX(Id) FROM Performance")
        result = cursor.fetchone()
        perf_id = result[0]

        cursor.execute("SELECT * FROM Performance WHERE Id = ?", (perf_id,))
        
        result = cursor.fetchone()
        conn.close()
        if result is None:
            return False
        else:
            api_key = 'e48976283ebb45a7ae1102438231003'
            date_api = datetime.today().strftime('%Y-%m-%d')
            hour = datetime.now().hour  

            url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={panels_adress}&dt={date_api}&hour={hour}"
            response = requests.get(url)
            data = response.json()

            temperature = data['forecast']['forecastday'][0]['hour'][0]['temp_c']
            wind_speed = data['forecast']['forecastday'][0]['hour'][0]['wind_kph']
            weather_type = data['forecast']['forecastday'][0]['hour'][0]['condition']['text']

            return SqliteDB.update_weather(perf_id, weather_type, temperature, wind_speed)


    #update weather data
    @staticmethod
    def update_weather(perf_id: int, weather_type: str, temperature: float, wind_speed: float) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d-%H')
        query = "INSERT INTO Weather (Perf_id, Weather_type, Date, Temperature, Wind_speed) VALUES (?, ?, ?, ?, ?)"
        values = (perf_id, weather_type, date_str, temperature, wind_speed)
        cursor.execute(query, values)
        conn.commit()

        cursor.execute("SELECT * FROM Weather WHERE Perf_id = ? AND Date = ?", (perf_id, date_str,))
        result = cursor.fetchone()
        conn.close()
        if result is None:
            return False
        else:
            return True
        
    
    #delete user
    @staticmethod
    def delete_user(user_id: int) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE Person_id = ?", (user_id,))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Users WHERE Person_id = ?", (user_id,))
            conn.commit()
            conn.close()
            return True
    

    # delete panels group
    @staticmethod
    def delete_panels(id_panel_group: int, person_id: int) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Panels WHERE Person_id = ? AND Id_PanelGroup = ?", (person_id, id_panel_group,))
        result = cursor.fetchone()

        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("SELECT Perf_id, Date FROM Performance WHERE Id_PanelGroup = ?", (id_panel_group,))
            perf_id_list = cursor.fetchall()
            for i in perf_id_list:
                if SqliteDB.delete_weather(i[0], i[1]):
                    SqliteDB.delete_performance(i[0], i[1])
                else:
                    conn.close()
                    return False
            cursor.execute("DELETE FROM Panels WHERE Person_id = ? AND Id_PanelGroup = ?", (person_id, id_panel_group,))
            conn.commit()
            conn.close()
            return True
    

    #delete performance
    @staticmethod
    def delete_performance(id: int, date: str) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Performance WHERE Date = ? AND Id = ?", (date, id,))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Performance WHERE Id = ? AND Date = ?", (id, date,))
            conn.commit()
            conn.close()
            return True

    # delete weather
    @staticmethod
    def delete_weather(perf_id: int, date: str) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Weather WHERE Perf_id = ? AND Date = ?", (perf_id, date))
        result = cursor.fetchone()

        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Weather WHERE Perf_id = ? AND Date = ?", (perf_id, date,))
            conn.commit()
            conn.close()
            return True
        
    #delete code
    @staticmethod
    def delete_code(code: int, email: str, date: str) -> bool:
        conn = sql.connect('C:\Solar Control\Solar_panels_server.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Codes WHERE Email = ? AND Code = ? AND Date = ?", (email, code, date,))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Codes WHERE Email = ? AND Code = ? AND Date = ?", (email, code, date,))
            conn.commit()
            conn.close()
            return True