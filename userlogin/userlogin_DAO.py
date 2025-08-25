import shared.connection as connection
from datetime import datetime,timedelta
import sqlite3


class UserLoginDAO:
    def login_authentication(username, password):
        con = connection.create_connection()
        cursor = None
        conn = None
        try: 
            conn = con.start_connection()
            
            if not conn :
                print("Database connection not available")
                return False
            
            cursor = conn.cursor()
            query = "SELECT * FROM login_info WHERE username = ?"
            cursor.execute(query, (username, ))
            user = cursor.fetchone()
                
            if not user or user[2] != password:    
                cursor.close()
                conn.close()
                print("Invalid username or password.")
                return False
            if user or user[2] == password:
                 print("found username or password.")
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Database error{e}")
            return False
        finally:
            if cursor:
                cursor.close
            if conn:
                conn.close