from precription_DAL import patientsDATA 
from shared.DTCpatientprescription import PatientPrescription
from typing import Dict, Optional

class prescription_model:
    def delete_prescription(prescription_id:str) -> bool:
        return patientsDATA.delete_patient_prescription(prescription_id)
    
    def update_prescription(self, prescription: PatientPrescription) -> bool:
        errors = self.check_validation(prescription)
        if errors:
            for field, error_msg in errors.items():
                print(f"Validation error in {field}: {error_msg}")
            return False
        success = patientsDATA.update_patient_prescription(prescription)
        if not success:
            print("Failed to update prescription in database")
        return success 
    
    def add_prescription(self , prescription : PatientPrescription) -> bool:
        errors = self.check_validation(prescription)
        if errors:
            for field , error_msg in errors.item():
                print(f"validation error in {field}: {error_msg}")        
            return False
        success = patientsDATA.add_patient_prescription(prescription)
        if not success:
            print("Failed to add data in the prescription in database")
        return success
    
    def check_validation(prescription: PatientPrescription) -> Optional[Dict[str, str]]:
        data = prescription.get_db_data()
        errors = {}
        if not data["prescription_id"] or data["prescription_id"].strip() == "":
            errors["prescription_id"] = "Prescription ID is required"
        
        if not data["patient_id"] or data["patient_id"].strip() == "":
            errors["patient_id"] = "Patient ID is required"
        
        if not data["medicine_id"] or data["medicine_id"].strip() == "":
            errors["medicine_id"] = "Medicine ID is required"
        
        if not data["dosage"] or data["dosage"].strip() == "":
            errors["dosage"] = "Dosage is required"
        
        if not data["frequency"] or data["frequency"].strip() == "":
            errors["frequency"] = "Frequency is required"
        
        if not data["duration"] or data["duration"].strip() == "":
            errors["duration"] = "Duration is required"
        
        if data["dosage"] and not any(char.isdigit() for char in data["dosage"]):
            errors["dosage"] = "Dosage should contain numeric values (e.g., '500mg')"
        
        if data["duration"] and not any(char.isdigit() for char in data["duration"]):
            errors["duration"] = "Duration should contain numeric values (e.g., '7 days')"
        
        return errors if errors else None