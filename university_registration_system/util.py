import datetime
import re
import config

def clear_screen():
    print("\n" * 3)

def divider(char = "-", length = 55):
    print(char * length)

def header(title):
    divider("=")
    print(f" {title.upper()}")
    divider("=")

def pause():
    input("\n Press Enter to continue.....")

def generate_student_id():
    config.student_counter += 1
    return f"STU{config.student_counter}"

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_age(age_str):
    try:
        age = int(age_str)
        return 15 <= age <= 60
    except ValueError:
        return False
    

def validate_dob(dob_str):

    try:
        datetime.datetime.strptime(dob_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def get_current_date():
    return datetime.datetime.now().strftime("%d/%m/%Y")

def get_current_datetime():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")