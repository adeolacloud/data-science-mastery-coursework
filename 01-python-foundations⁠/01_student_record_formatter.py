# 01_student_record_formatter.py

def format_student_records(students):
    print("=" * 55)
    print(f"{'STUDENT NAME':<20} | {'GPA':<8} | {'STATUS':<15}")
    print("=" * 55)
    
    for student in students:
        name = student.get("name", "N/A")
        gpa = float(student.get("gpa", 0.0))
        status = "Honors" if gpa >= 3.5 else "Standard"
        print(f"{name:<20} | {gpa:<8.2f} | {status:<15}")
        
    print("=" * 55)

if __name__ == "__main__":
    sample_students = [
        {"name": "Adeola Rasheed", "gpa": 3.85},
        {"name": "Adeshewa Bakare", "gpa": 3.40},
        {"name": "Kudirat Adeyanju", "gpa": 3.92}
    ]
    format_student_records(sample_students)
