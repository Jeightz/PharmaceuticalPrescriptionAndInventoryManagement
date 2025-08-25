from precription_model import prescription_model
class prescriptionController():
    def req_add_prescription(prescription) -> None :
        sucess = prescription_model.add_prescription(prescription)
        if sucess:
            print("successfully add")
    
    def req_update_prescription(prescription)-> None:    
        sucess = prescription_model.update_prescription(prescription) 
        if sucess :
            print("successfuly updated")
            
    def req_delete_prescription(prescription_id)-> None: 
        sucess = prescription_model.delete_prescription(prescription_id)
        if sucess:
            print("sucesssfully deleted")