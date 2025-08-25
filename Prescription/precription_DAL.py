from shared.connection import create_connection as con
import sqlite3
from shared.DTCpatientprescription import PatientPrescription  
from typing import Dict, Optional, List, Tuple
from datetime import datetime

class patientsDATA:
    @classmethod
    def get_all_patients_prescription_that_status_pending(cls) -> Optional[List[PatientPrescription]]:
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return None
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patient_prescription WHERE status = 'pending' ORDER BY date DESC"
            cursor.execute(query)
            prescriptions = cursor.fetchall()
            
            return [PatientPrescription.from_db_datarow(row) for row in prescriptions]
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            if conn:
                conn.close()
    
    @classmethod
    def get_all_patients_prescriptions(cls) -> List[PatientPrescription]:
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return []
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patient_prescription ORDER BY date DESC"
            cursor.execute(query)
            prescriptions = cursor.fetchall()
            
            return [PatientPrescription.from_db_datarow(row) for row in prescriptions]
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            if conn:
                conn.close()
    
    @classmethod
    def get_prescriptions_by_status(cls, status: str) -> List[PatientPrescription]:
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return []
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patient_prescription WHERE status = ? ORDER BY date DESC"
            cursor.execute(query, (status,))
            prescriptions = cursor.fetchall()
            
            return [PatientPrescription.from_db_datarow(row) for row in prescriptions]
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            if conn:
                conn.close()
    
    @classmethod
    def get_prescriptions_by_patient_id(cls, patient_id: str) -> List[PatientPrescription]:
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return []
        
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM patient_prescription WHERE patient_id = ? ORDER BY date DESC"
            cursor.execute(query, (patient_id,))
            prescriptions = cursor.fetchall()
            
            return [PatientPrescription.from_db_datarow(row) for row in prescriptions]
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            if conn:
                conn.close()
    
    @classmethod
    def add_patient_prescription(cls, prescription: PatientPrescription) -> bool:
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return False
        
        try:
            # Extract data from the prescription object
            data = prescription.get_db_data()
            
            cursor = conn.cursor()
            query = """INSERT INTO patient_prescription 
                      (prescription_id, patient_id, medicine_id, dosage, frequency, 
                       duration, special_instruction, status, date) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (
                data["prescription_id"],
                data["patient_id"],
                data["medicine_id"],
                data["dosage"],
                data["frequency"],
                data["duration"],
                data.get("special_instruction", "None"),
                data.get("status", "pending"),  # Default to pending
                data.get("date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # Current timestamp
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
    def update_patient_prescription(cls, prescription: PatientPrescription) -> bool:
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
                      SET medicine_id = ?, dosage = ?, frequency = ?, duration = ?, 
                          special_instruction = ?, status = ?, date = ?
                      WHERE prescription_id = ?"""
            cursor.execute(query, (
                data["medicine_id"],
                data["dosage"],
                data["frequency"],
                data["duration"],
                data.get("special_instruction", "None"),
                data.get("status", "pending"),
                data.get("date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
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
    def update_prescription_status(cls, prescription_id: str, status: str) -> bool:
        """Update only the status of a prescription"""
        conn = con.start_connection()
        
        if not conn:
            print("Database connection not available")
            return False
        
        try:
            cursor = conn.cursor()
            query = "UPDATE patient_prescription SET status = ? WHERE prescription_id = ?"
            cursor.execute(query, (status, prescription_id))
            
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
    def delete_patient_prescription(cls, prescription_id: str) -> bool:
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
    
