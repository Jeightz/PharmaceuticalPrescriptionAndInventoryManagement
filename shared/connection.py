import mysql.connector


class create_connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    def start_connection(self):
        self
        return self._connect()
    
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
    