
def add_student(name,age,marks):
    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "average": sum(marks) / len(marks)
    }

    students.append(student)

def display_students():
    for student in students:
        print("\nStudent Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("Average:", round(student["average"], 2))

students = []


add_student("Hari", 22, [85, 90, 78])
add_student("Arun", 21, [75, 80, 88])

display_students()