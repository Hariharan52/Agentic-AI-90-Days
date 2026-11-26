
import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with empty records.")
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students, name, age, marks):
    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "average": sum(marks) / len(marks)
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("Average:", round(student["average"], 2))


students = load_students()

while True:
    print("\n--- Student Records Manager ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            name = input("Enter student name: ")
            age = int(input("Enter age: "))

            marks = []

            for i in range(1, 4):
                mark = float(input(f"Enter subject {i} mark: "))

                if not 0 <= mark <= 100:
                    raise ValueError("Marks must be between 0 and 100.")

                marks.append(mark)

            add_student(students, name, age, marks)

        except ValueError as error:
            print("Invalid input:", error)

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        print("Thank you for using Student Records Manager!")
        break

    else:
        print("Invalid choice. Try again.")
