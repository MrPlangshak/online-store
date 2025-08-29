students_db = {}   # dictionary to store students
print(students_db)

def start():
    while True:
        print('''
        1. Add student
        2. Delete student
        3. Update student record
        4. Get a student by ID
        5. Display all students
        6. Search students by name
        7. Count students
        8. Filter by age
        9. Exit
        ''')
        try:
            user_choice = int(input("Enter choice:\n"))
        except ValueError:
            print("Invalid input, please enter a number")
            continue

        if user_choice == 1:
            add_students()
        elif user_choice == 2:
            delete_student()
        elif user_choice == 3:
            update_student()
        elif user_choice == 4:
            get_student()
        elif user_choice == 5:
            display_students()
        elif user_choice == 6:
            search_student()
        elif user_choice == 7:
            count_student()
        elif user_choice == 8:
            filter_by_age()
        elif user_choice == 9:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Add a student
def add_students():
    name = input("Enter student name:\n")
    age = int(input("Enter student age:\n"))
    department = input("Enter student department:\n")
    key = len(students_db) + 1
    students_db[key] = {"name": name, "age": age, "department": department}
    print("Student added successfully.")
    print(students_db)

# Delete a student
def delete_student():
    student_id = int(input("Enter student id:\n"))
    if student_id in students_db:
        del students_db[student_id]
        print(f"Student id {student_id} deleted successfully")
    else:
        print("ID not found")

# Update a student
def update_student():
    print(''' 
    1. Update name
    2. Update age 
    3. Update department
    ''')
    command = int(input("Enter command:\n"))
    if command < 1 or command > 3:
        print("Invalid command")
        return

    student_id = int(input("Enter student id to update:\n"))
    if student_id not in students_db:
        print("ID not found")
        return

    if command == 1:
        name = input("Enter new name:\n")
        students_db[student_id]["name"] = name
    elif command == 2:
        age = int(input("Enter new age:\n"))
        students_db[student_id]["age"] = age
    elif command == 3:
        department = input("Enter new department:\n")
        students_db[student_id]["department"] = department
    
    print("Record updated successfully.")
    print(students_db)

# Get student by ID
def get_student():
    student_id = int(input("Enter student id:\n"))
    if student_id in students_db:
        student = students_db[student_id]
        print(f"{student['name']} {student['age']} {student['department']}")
    else:
        print("ID not found")

# Display all students
def display_students():
    if not students_db:
        print("No students found.")
    else:
        for sid, student in students_db.items():
            print(f"{sid}: {student['name']}, {student['age']}, {student['department']}")

# Search students by name
def search_student():
    search = input("Enter student name:\n").lower()
    found = False
    for student_id, student in students_db.items():
        if search in student["name"].lower():
            print(f"{student['name']}, {student['age']}, {student['department']}")
            found = True
    if not found:
        print("Name not found, try again")

# Count students
def count_student():
    print(f"Total students: {len(students_db)}")

# Filter by age
def filter_by_age():
    limit = int(input("Enter minimum age:\n"))
    if limit < 0:
        print("Invalid age limit")
        return

    found = False
    for student_id, student in students_db.items():
        if student["age"] >= limit:
            print(f"{student['name']}, {student['age']}, {student['department']}")
            found = True
    if not found:
        print("No student found above this age.")

# Start the program
start()
