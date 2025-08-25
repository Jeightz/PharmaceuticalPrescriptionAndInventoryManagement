from typing import Dict, Optional
from datetime import datetime

class PatientPrescription:
    def __init__(self, prescription_id: str, patient_id: str, medicine_id: str, 
                 dosage: str, frequency: str, duration: str, 
                 special_instruction: str = "NONE", status: str = "pending", 
                 date: Optional[str] = None):
        self.prescription_id = prescription_id
        self.patient_id = patient_id
        self.medicine_id = medicine_id
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        self.special_instruction = special_instruction
        self.status = status  # 'pending' or 'complete'
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @classmethod
    def from_db_datarow(cls, row):
        return cls(
            row[0],  # prescription_id
            row[1],  # patient_id
            row[2],  # medicine_id
            row[3],  # dosage
            row[4],  # frequency
            row[5],  # duration
            row[6],  # special_instruction
            row[7],  # status
            row[8]   # date
        )
    
    def get_db_data(self) -> Dict[str, str]:
        return {
            "prescription_id": self.prescription_id, 
            "patient_id": self.patient_id,
            "medicine_id": self.medicine_id,
            "dosage": self.dosage,
            "frequency": self.frequency,
            "duration": self.duration,
            "special_instruction": self.special_instruction,
            "status": self.status,
            "date": self.date
        }
    
    def to_db_tuple(self) -> tuple:
        return (
            self.prescription_id, 
            self.patient_id, 
            self.medicine_id,
            self.dosage, 
            self.frequency, 
            self.duration, 
            self.special_instruction,
            self.status,
            self.date
        )
    
    def mark_as_complete(self):
        """Mark prescription as complete with current timestamp"""
        self.status = "complete"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def is_pending(self) -> bool:
        """Check if prescription is pending"""
        return self.status == "pending"
    
    def is_complete(self) -> bool:
        """Check if prescription is complete"""
        return self.status == "complete"