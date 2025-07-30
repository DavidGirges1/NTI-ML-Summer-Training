class Student:
    def __init__(self, name, age, grade, contact):
        self.name = name
        self.age = age
        self.grade = grade
        self.contact = contact

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("Contact:", self.contact)
        print("-------------")


students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    contact = input("Enter contact: ")
    student = Student(name, age, float(grade), contact)
    students.append(student)
    print("Student added.\n")

def show_students():
    if len(students) == 0:
        print("No students yet.\n")
    else:
        for s in students:
            s.show()

def update_student():
    name = input("Enter name of student to update: ")
    for s in students:
        if s.name == name:
            new_name = input("New name (or press Enter to keep same): ")
            new_age = input("New age: ")
            new_grade = input("New grade: ")
            new_contact = input("New contact: ")
            if new_name != "":
                s.name = new_name
            s.age = new_age
            s.grade = float(new_grade)
            s.contact = new_contact
            print("Student updated.\n")
            return
    print("Student not found.\n")

def average_grade():
    if len(students) == 0:
        print("No students yet.\n")
    else:
        total = 0
        for s in students:
            total += s.grade
        avg = total / len(students)
        print("Average grade:", avg, "\n")

def top_student():
    if len(students) == 0:
        print("No students yet.\n")
    else:
        high = max(s.grade for s in students)
        print("Top student(s):")
        for s in students:
            if s.grade == high:
                s.show()

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Average Grade")
    print("5. Top Student(s)")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        average_grade()
    elif choice == "5":
        top_student()
    elif choice == "6":
        print("Bye!")
        break
    else:
        print("Invalid choice.\n")