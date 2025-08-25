from typing import Dict, Optional

class PatientPrescription:
    def __init__(self, prescription_id: str, patient_id: str, medicine_id: str, 
                 dosage: str, frequency: str, duration: str, special_instruction: str = "NONE"):
        self.prescription_id = prescription_id
        self.patient_id = patient_id
        self.medicine_id = medicine_id
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        self.special_instruction = special_instruction
    
    @classmethod
    def from_db_datarow(cls, row):
        return cls(*row)
    
    def get_db_data(self) -> Dict[str, str]:
        return {
            "prescription_id": self.prescription_id, 
            "patient_id": self.patient_id,
            "medicine_id": self.medicine_id,
            "dosage": self.dosage,
            "frequency": self.frequency,
            "duration": self.duration,
            "special_instruction": self.special_instruction  # Fixed typo
        }
    
    def to_db_tuple(self) -> tuple:
        return (
            self.prescription_id, 
            self.patient_id, 
            self.medicine_id,
            self.dosage, 
            self.frequency, 
            self.duration, 
            self.special_instruction
        )