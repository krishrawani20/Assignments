
members = []

def register_member(name):
    members.append(name)
    print("Member Registered Successfully")

def display_members():
    if len(members) == 0:
        print("No Members Registered")
    else:
        print("\nRegistered Members:")
        for member in members:
            print(member)