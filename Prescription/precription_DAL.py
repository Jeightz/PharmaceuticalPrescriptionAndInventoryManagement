from shared.connection import create_connection as con
import sqlite3
from shared.DTCpatientprescription import PatientPrescription  

class patientsDATA:
    
    @classmethod
    def get_all_patients_prescriptions(cls):
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return []
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patient_prescription"
            cursor.execute(query)
            prescriptions = cursor.fetchall()
            
            return prescriptions
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            if conn:
                conn.close()
    
    @classmethod
    def add_patient_prescription(cls, prescription: PatientPrescription):
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return False
        
        try:
            # Extract data from the prescription object
            data = prescription.get_db_data()
            
            cursor = conn.cursor()
            query = """INSERT INTO patient_prescription 
                      (prescription_id, patient_id, medicine_id, dosage, frequency, duration, special_instruction) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (
                data["prescription_id"],
                data["patient_id"],
                data["medicine_id"],
                data["dosage"],
                data["frequency"],
                data["duration"],
                data.get("special_instruction", "None")
            ))
            
            if cursor.rowcount == 0:
                print("Failed to add prescription")
                return False
                    
            conn.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                conn.close()
    
    @classmethod
    def update_patient_prescription(cls, prescription: PatientPrescription):
        """Update an existing prescription using PatientPrescription data class"""
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return False
        
        try:
            # Extract data from the prescription object
            data = prescription.get_db_data()
            
            cursor = conn.cursor()
            query = """UPDATE patient_prescription 
                      SET medicine_id = ?, dosage = ?, frequency = ?, duration = ?, special_instruction = ?
                      WHERE prescription_id = ?"""
            cursor.execute(query, (
                data["medicine_id"],
                data["dosage"],
                data["frequency"],
                data["duration"],
                data.get("special_instruction", "None"),
                data["prescription_id"]
            ))
            
            if cursor.rowcount == 0:
                print("No prescription found to update")
                return False
                
            conn.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                conn.close()
    
    @classmethod
    def delete_patient_prescription(cls, prescription_id):
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return False
        
        try:
            cursor = conn.cursor()
            query = "DELETE FROM patient_prescription WHERE prescription_id = ?"
            cursor.execute(query, (prescription_id,))
            
            if cursor.rowcount == 0:
                print("No prescription found to delete")
                return False
                
            conn.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return False
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