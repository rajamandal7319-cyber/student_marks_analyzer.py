print("===== STUDENT MANAGEMENT SYSTEM =====")

students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Student name: ")
        age = input("Student age: ")
        course = input("Course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added!")

    elif choice == "2":
        print("\n===== STUDENTS =====")

        if len(students) == 0:
            print("No students yet.")
        else:
            for i, student in enumerate(students, 1):
                print(
                    i, ".",
                    student["name"],
                    "| Age:", student["age"],
                    "| Course:", student["course"]
                )

    elif choice == "3":
        name = input("Search student name: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        if len(students) == 0:
            print("No students to delete.")
        else:
            for i, student in enumerate(students, 1):
                print(i, ".", student["name"])

            number = int(input("Kaunsa student delete karna hai? "))

            if 1 <= number <= len(students):
                deleted = students.pop(number - 1)
                print("Deleted:", deleted["name"])
            else:
                print("Invalid student number.")

    elif choice == "5":
        print("Student Management System closed.")
        break

    else:
        print("Invalid option.")

print("Powered by : RAJ.K.M ©")