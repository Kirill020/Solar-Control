import sqlite3 as sql
import hashlib

class SqliteDB:


    #authentication user
    @staticmethod
    def authenticate_user(username: str, password: str) -> bool:
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        cursor.execute("SELECT P_pass FROM Users WHERE P_name = ?", (username,))
        result = cursor.fetchone()

        if result is None:
            conn.close()
            return False

        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

        if password_hash == result[0]:
            conn.close()
            return True

        conn.close()
        return False


    #add user
    @staticmethod
    def add_user(P_name: str, P_email_adress: str, P_adress: str, Password: str):
        conn = sql.connect("Solar_panel.db")
        cursor = conn.cursor()
        P_pass  = hashlib.sha256(Password.encode('utf-8')).hexdigest()
        cursor.execute("INSER INTO Users (P_name, P_email_adress, P_adress, P_pass) VALUES (?, ?, ?, ?)", (P_name, P_email_adress, P_adress, P_pass))
        conn.commit()
        conn.close()
    
    #add panel group
    @staticmethod
    def add_panels_group(person_id: int, panels_amount: int, panels_adress: str, performance: float, m_performance: float, w_performance: float, d_performance: float):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        query = "INSERT INTO Panels (Person_id, Panels_amount, Panels_adress, Performance, M_performance, W_performance, D_performance) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (person_id, panels_amount, panels_adress, performance, m_performance, w_performance, d_performance)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    #add weather data
    @staticmethod
    def add_weather_data(id_panels_group: int, weather_type: str, date: str, temperature: float, wind_speed: float):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        query = "INSERT INTO Weather (Id_PanelsGroup, Weather_type, Date, Temperature, Wind_speed) VALUES (?, ?, ?, ?, ?)"
        values = (id_panels_group, weather_type, date, temperature, wind_speed)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    #update user info
    @staticmethod
    def update_user_data(Person_id: int, new_name: str, new_email_adress: str, new_adress:str, new_pass: str):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        if(new_name != None):
            query = "UPDATE Users SET P_name = {new_name} WHERE Person_id = {Person_id}"
            cursor.execute(query)
            conn.commit()
            conn.close()

        elif(new_email_adress != None):
            query = "UPDATE Users SET P_email_adress = {new_email_adress} WHERE Person_id = {Person_id}"
            cursor.execute(query)
            conn.commit()
            conn.close()
        
        elif(new_adress != None):
            query = "UPDATE Users SET P_adress = {new_adress} WHERE Person_id = {Person_id}"
            cursor.execute(query)
            conn.commit()
            conn.close()

        elif(new_pass != None):
            P_pass  = hashlib.sha256(new_pass.encode('utf-8')).hexdigest()
            query = "UPDATE Users SET P_pass = {P_pass} WHERE Person_id = {Person_id}"
            cursor.execute(query)
            conn.commit()
            conn.close()
        


    #update panels data
    #todo:      change DB(Panels) and set power, voltage and power
    #           and change next method
    
    @staticmethod
    def update_penels_group(Panels_id: int):
        conn = sql.connect('Solar_panel.db')
        cursor = conn.cursor()
        query = "UPDATE Panels SET Performance = {P_pass} WHERE Id_PanelGroup = {Panels_id}"
        #cursor.execute(query)
        conn.commit()
        conn.close()

    #@staticmethod
    #def upd_user()
