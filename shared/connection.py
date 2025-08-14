import mysql.connector
from dotenv import load_dotenv
import os
from pathlib import Path

class create_connection:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        env_path = Path(__file__).parent / "others.env"  
        load_success = load_dotenv(dotenv_path=env_path)
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = os.getenv("DB_PORT", 3307)  
        self.connection = None

    def start_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connection = self._connect()
        return self.connection

    def close_connection(self, exc_type=None, exc_value=None, exc_traceback=None):
        if exc_type:
            print(f"Error type: {exc_type}")    
            print(f"Error value: {exc_value}")   
            print(f"Traceback: {exc_traceback}")       
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        return False

    def _connect(self):
        try:
            
            con = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                auth_plugin='mysql_native_password', 
                use_pure=True
            )


            cursor = con.cursor()
            cursor.execute("SHOW DATABASES;")
            databases = [db[0] for db in cursor.fetchall()]

            if self.database not in databases:
                print(f"❌ Database '{self.database}' does NOT exist.")
                con.close()
                return None


            if con.is_connected():
                print(f"✅ Connected to database '{self.database}' on port {self.port}")
                return con

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
