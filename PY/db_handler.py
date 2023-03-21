import sqlite3 as sql

class SqliteDB:

    @staticmethod
    def add_user(P_name, P_email_adress):
        conn = sql.connect("Solar_panel.db")
        cursor = conn.cursor()
        cursor.execute("INSER INTO People (P_name, P_email_adress) VALUES (?, ?)", (P_name, P_email_adress))
        conn.commit()
        conn.close()
    
    @staticmethod
    def add_panel_group(Panels_amount, Panels_adress, Capasity):
        conn = sql.connect("Solar_panel.db")
        cursor = conn.cursor()
        cursor.execute("INSER INTO Panels (Panels_amount, Panels_adress, Capasity) VALUES (?, ?, ?)", (Panels_amount, Panels_adress, Capasity))
        conn.commit()
        conn.close()
    
    
