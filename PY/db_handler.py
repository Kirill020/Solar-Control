import sqlite3 as sql
import hashlib
from datetime import datetime

class SqliteDB:

    # todo: sql-query to get an Id from Weather and Panels

    #authentication user
    @staticmethod
    def authenticate_user(username: str, password: str) -> tuple[bool, int]:
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT P_pass, Person_id FROM Users WHERE P_name = ?", (username,))
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


    #get wetaher_id
    @staticmethod
    def get_weather_id(id_panel_group: int) -> int:
        conn = sql.connect("Solar_panel.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Weather_id FROM Weather WHERE Id_PanelGroup = ?", (id_panel_group,))
        conn.commit()
        
        result = cursor.fetchone()
        if result is None:
            conn.close()
            return None
        else:
            conn.close()
            return result[0]
        
    
    @staticmethod
    def get_panel_group_id(person_id: int) -> int:
        conn = sql.connect("Solar_panel.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Id_PanelGroup FROM Panels WHERE Person_id = ?", (person_id,))
        
        result = cursor.fetchone()
        if result is None:
            conn.close()
            return None
        else:
            conn.close()
            return result[0]

    
    #add user
    @staticmethod
    def add_user(p_name: str, p_email_adress: str, p_adress: str, password: str):
        conn = sql.connect("Solar_panel.db")
        cursor = conn.cursor()
        p_pass  = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cursor.execute("INSERT INTO Users (P_name, P_email_adress, P_adress, P_pass) VALUES (?, ?, ?, ?)", (p_name, p_email_adress, p_adress, p_pass))
        conn.commit()
        conn.close()
    
    #add panel group
    @staticmethod
    def add_panels_group(person_id: int, panels_amount: int, panels_adress: str, performance: float, voltage: float, power: float):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        date = datetime.now()
        query = "INSERT INTO Panels (Person_id, Panels_amount, Panels_adress, Performance, Voltage, Power, Date) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (person_id, panels_amount, panels_adress, performance, voltage, power, date)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    #add weather data
    @staticmethod
    def add_weather_data(id_panels_group: int, weather_type: str, temperature: float, wind_speed: float):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        date = datetime.now()
        query = "INSERT INTO Weather (Id_PanelsGroup, Weather_type, Date, Temperature, Wind_speed) VALUES (?, ?, ?, ?, ?)"
        values = (id_panels_group, weather_type, date, temperature, wind_speed)
        cursor.execute(query, values)
        conn.commit()
        conn.close()


    #update user info
    @staticmethod
    def update_user_data(person_id: int, new_name: str, new_email_adress: str, new_adress: str, new_pass: str) -> bool:
        conn = sql.connect('Solar_panel.db')
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

        cursor.execute("SELECT COUNT(*) FROM Users WHERE Person_id = ? LIMIT 1", (person_id,))
        result = cursor.fetchone()
        conn.close()

        return result[0] == 1

        

    #update panels data
    @staticmethod
    def update_penels_group(panels_id: int, person_id: int, panels_amount: int, panels_adress: str, performance: float, voltage: float, power: float):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        date = datetime.now()
        query = "INSERT INTO Panels (Id_PanelGroup, Person_id, Panels_amount, Panels_adress, Performance, Voltage, Power, Date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        values = (panels_id, person_id, panels_amount, panels_adress, performance, voltage, power, date)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    #update weather data
    @staticmethod
    def update_weather(weather_id: int, id_panels_group: int, weather_type: str, temperature: float, wind_speed: float):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        date = datetime.now()
        query = "INSERT INTO Weather (Weather_id, Id_PanelsGroup, Weather_type, Date, Temperature, Wind_speed) VALUES (?, ?, ?, ?, ?, ?)"
        values = (weather_id, id_panels_group, weather_type, date, temperature, wind_speed)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
    
    #delete user
    @staticmethod
    def delete_user(person_id: int) -> bool:
        conn = sql.connect('Solar_panel.db')
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
    def delete_panels(id_panel_group: int, person_id: int) -> bool:
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Panels WHERE Person_id = ? AND Id_PanelGroup = ?", (person_id, id_panel_group))
        result = cursor.fetchone()
        
        if result is None:
            conn.close()
            return False

        else:
            cursor.execute("DELETE FROM Panels WHERE Person_id = ? AND Id_PanelGroup = ?", (person_id, id_panel_group))
            conn.commit()
            conn.close()
            return True