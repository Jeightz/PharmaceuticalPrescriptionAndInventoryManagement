import shared.connection as con
from datetime import datetime,timedelta

conn = con.start_connection()


class UserLoginDAO:
    def login_authentication(username, password):
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username, ))
        user = cursor.fetchone()
        
        if not user or user['password'] != password:    
            cursor.close()
            conn.close()
            print("Invalid username or password.")
            return False
        if user['locked_until'] and user['locked_until'] > datetime.now():
            return f"Account locked until {user['locked_until']}"
    
        conn.commit()
        cursor.close()
        conn.close()
        return True
    