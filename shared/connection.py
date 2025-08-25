from pathlib import Path
import sqlite3

class create_connection:
    def __init__(self):
        self.connection = None
        self.db_path = Path(__file__).parent.parent / "pharmaceuticaldb.db"

    def start_connection(self):
        if not self.connection:
            self.connection = self._connect()
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Database connection closed.")

    def _connect(self):
        try:
            print(f"🔍 Looking for database at: {self.db_path}")
            
            if not self.db_path.exists():
                print(f"❌ Database file not found: {self.db_path}")
                return None
            
            print(f"✅ Database file found!")
            
            con = sqlite3.connect(self.db_path)
            
            cursor = con.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()  
            
            print(f"📊 Found {len(tables)} tables in database:")
            for table in tables:
                print(f"  - {table[0]}")
            
            print("✅ Connected to database successfully!")
            return con
            
        except sqlite3.Error as err:
            print(f"❌ SQLite connection error: {err}")
            return None
        except Exception as err:
            print(f"❌ Unexpected error: {err}")
            return None