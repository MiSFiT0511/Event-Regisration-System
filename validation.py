import re

def validate_name(name):
    return re.match(r"^[A-Za-z ]+$", name)

def validate_age(age):
    try:
        age = int(age)
        return 18 <= age <= 100
    except:
        return False

def validate_email(email):
    return re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email)