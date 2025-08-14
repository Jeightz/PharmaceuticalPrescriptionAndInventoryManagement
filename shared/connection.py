import mysql.connector
from dotenv import load_dotenv 
import os

class create_connection:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.connection = None
        
    def start_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connection = self._connect()
        return self.connection

        
    def close_connection(self,exc_type,exc_value,exc_traceback):
        if exc_type:
            print(f"Error type: {exc_type}")    
            print(f"Error value: {exc_value}")   
            print(f"Traceback: {exc_traceback}")       
        if self.connection:
            self.connection.close()
        return False
    
    def _connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            connection.autocommit
            if connection.is_connected():
                print("Connection to the database was successful.")
                return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
    