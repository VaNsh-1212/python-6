student_marks = {
    "alice": 85,
    "bob": 90,
    "vansh": 95
}
name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")