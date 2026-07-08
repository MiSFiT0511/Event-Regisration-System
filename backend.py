import database
import validation

def register_participation(name, age, email):
    if not validation.validate_name:
        return{"success": False,"message": "Invalid name"}
    
def register_participation(name, age, email):
    if not validation.validate_age:
        return{"success": False,"message": "Invalid age"}
    
def register_participation(name, age, email):
    if not validation.validate_email:
        return{"success": False,"message": "Invalid email"}
    
    database.save_participant(name, age, email)
    return{"success": True, "message": "Registration succesful"}