import sqlite3
from shared.connection import create_connection as con
class prescription_DAO:
    @classmethod
    def check_id_dup(cls,uuid) -> bool:
        conn  = con.start_connection()
        
        if not conn:
            print("Database connecttion not available")
            return None
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patients_prescriptions WHERE prescription_id = ?"
            cursor.execute(query,(uuid,))
            success = cursor.fetchall()
            
            
            return result is not None

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()
                                    
    @classmethod
    def get_all_patient_prescription_by_patientid(cls, patient_id) -> bool:
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return None
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patient_prescription WHERE patient_id = ?"
            cursor.execute(query, (patient_id,))
            prescription = cursor.fetchone()
            
            return prescription
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()
            
    @classmethod
    def get_prescription_by_id(cls, prescription_id):
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return None
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patient_prescription WHERE prescription_id = ?"
            cursor.execute(query, (prescription_id,))
            prescription = cursor.fetchone()
            
            return prescription
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()