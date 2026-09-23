import config
from util import divider, clear_screen, get_current_datetime

def display_courses():
    print("\n Availlable Courses: ")
    divider("-")
    for key, val in config.courses.items():
        print(f" {key}. {val['name']} | {val['duration']} | Rs. {val['fee']:,}/year")
    divider("-")


def print_student_card(sid, s, detailed = False):
    divider("-")
    print(f"  Student ID  : {sid}")
    print(f"  Name         : {s['name']}")
    print(f"  Age / Gender : {s['age']} / {s['gender']}")
    print(f"  Course       : {s['course']}")
    print(f"  Status       : {s['status'].upper()}")
    if detailed:
        print(f"  DOB          : {s['dob']}")
        print(f"  Phone        : {s['phone']}")
        print(f"  Email        : {s['email']}")
        print(f"  Address      : {s['address']}")
        print(f"  Qualification: {s['qualification']}")
        print(f"  Annual Fee   : Rs. {s['fee']:,.0f}")
        print(f"  Registered On: {s['reg_date']}")
    divider("-")
