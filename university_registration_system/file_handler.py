import csv
import os
import config

def save_data():
    try:
        with open(config.DATA_FILE, "w", newline="") as f:
            fieldnames = [
                "student_id", "name", "age", "gender", "dob",
                "phone", "email", "address", "course", "qualification",
                "password", "status", "req_date", "fee"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for sid, data in config.students.items():
                row = {"student_id": sid}
                row.update(data)
                writer.writerow(row)
        print(" Data saved successfully")
    except Exception as e:
        print(f" Error saving data: {e}")

def load_data():
    if not os.path.exists(config.DATA_FILE):
        return
    try:
        with open(config.DATA_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sid = row.pop("student_id")
                row["age"] = int(row["age"])
                row["fee"] = float(row["fee"])
                config.students[sid] = row
                num = int(sid.replace("STU", ""))
                if num >= config.student_counter:
                    config.student_counter = num + 1

        print(f" Loaded {len(config.students)} student record from file.")
    except Exception as e:
        print(f"Error loading data: {e}")