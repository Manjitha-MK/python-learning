students = {
    "Alice": 85,
    "Bob": 92,  
    "Charlie": 78,
    "David": 88
}

# Add a new student "Amal" with marks 90
students["Amal"] = 90

print(students)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88, 'Amal': 90}

# Search students
name = "Alice"

if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

# Update students
students["Bob"] = 94
print(students)

# Delete student
del students["Amal"]
print(students)


# def add_students(name, marks):
#     students[name] = marks

# add_students("Amal", 33)

# print(students)

def view_students():
    if not students:
        print("No students to view.")
        return
    print("\n-------Student List------")
    for names, marks in students.items():
        print(names,"-", marks)

view_students()

print("-----------------------------------")
def search_student(name):
    if name in students:
        print(name, "found")
        print(name,"Marks:", students[name])
        return
    else:
        print(name, "Not found")

search_student("Kamal")
search_student("Amal")

print("------------------------------------")
def update_marks(name, new_marks):
    if name in students:
        students[name] = new_marks
        print(name, "marks updated successfully")
    else:
        print(name, "not found")

update_marks("Amal", 44)
update_marks("Kamal", 32)
print(students)

print("------------------------------------")
def delete_student(name):
    if name in students:
        del students[name]
        print(name, "deleted successfully.")
    else:
        print(name, "not found")

delete_student("Alice")
delete_student("Manji")
print(students)

print("------------------------------------")

def add_student(name, marks):
    if name in students:
        print(name, "already exists !...")
    else:
        students[name] = marks
        print(name, "successfully added !...")

add_student("Alice", 93)
add_student("Manji", 92)

print(students)

print("------------------------------------")


def calculate_average(students):
    total = 0
    avg = 0
    if len(students) == 0:
        print("dictionary is empty")
        return

    for marks in students.values():
        total += marks
        avg = total/len(students)
    return total,avg

tot,avg = calculate_average(students)

print("Total marks is:", tot)
print(len(students))
print("Average is:", avg)

print("------------------------------------")
def find_top_students(students):
    if not students:
        print("No students available.")
        return None, None
    
    highest_marks = 0
    for names, marks in students.items():
        if highest_marks < marks:
            highest_marks = marks
            top_student = names
    return top_student, highest_marks

ts,hm = find_top_students(students)

print("Top student is",ts, "and marks is", hm)

print("-----------------------------------------")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update student marks")
    print("5. Delete student")
    print("6. Find top student")
    print("7. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        try:
            marks = int(input("Enter student marks: "))

            if 0 <= marks <= 100:
                add_student(name, marks)
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter valid marks!")

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter student name to search: ")
        search_student(name)

    elif choice == "4":
        name = input("Enter name: ")
        new_marks = int(input("Enter new marks: "))
        update_marks(name, new_marks)

    elif choice == "5":
        name = input("Enter student name: ")
        delete_student(name)

    elif choice == "6":
        print("option 6 is working")
        ts,hm = find_top_students(students)
        if ts is not None:
            print("Top student is", ts, "and marks is", hm)

    elif choice == "7":
        print("Good bye...")
        break

    else:
        print("Invalid input")




    