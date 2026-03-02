import re

def validate_student(student_id, name, email, mobile):
    if not student_id or not name:
        return "Student ID and Name are required"

    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid Email Format"

    if mobile and (not mobile.isdigit() or len(mobile) != 10):
        return "Mobile number must be 10 digits"

    return None
