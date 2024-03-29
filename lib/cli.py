# lib/cli.py

from helpers import (
    exit_program,
    create_initial_table, 
    list_courses, 
    create_new_course,
    find_course_by_subject,
    create_initial__student_table,
    list_of_students,
    find_student_by_name,
    create_new_student,
    create_and_add_new_student,
    update_student_information,
    expel_student,
)


def main():
    create_initial_table()

    while True:
        menu()
        choice = input(">> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            courses()
        elif choice == "2":
            students()
        else:
            print("Invalid choice")

def courses():
    while True:
        submenu_courses()
        choice = input(">> ")
        if choice == "0":
            break
        elif choice == "1":
            list_courses()
        elif choice == "2":
            create_new_course()
        elif choice == "3":
            find_course_by_subject()
        elif choice == "4":
            create_and_add_new_student()
        else:
            print("Invalid choice")

def students():
    create_initial__student_table()

    while True:
        submenu_students()
        choice = input(">> ")

        if choice == "0":
            break
        elif choice == "1":
            list_of_students()
        elif choice == "2":
            find_student_by_name()
        elif choice == "3":
            create_new_student()
        elif choice == "4":
            update_student_information()
        elif choice == "5":
            expel_student()
        else:
            print("Invalid Choice")

#####################
            
def menu():
    print("Please select an option:")
    print("0. Exit the Program")
    print("1. Courses Menu")
    print("2. Students Menu")

def submenu_courses():
    print("Welcome to the Courses Menu. What would you like to do?")
    print("1. List of Courses")
    print("2. Create New Course")
    print("3. Search for Course by Subject")
    print("4. Create and Add New Student")
    print("0. Go back")

def submenu_students():
    print("Welcome to the Students Menu. What would you like to do?")
    print("0. Go Back")
    print("1. List of Students")
    print("2. Search for Student by Name")
    print("3. Create New Student")
    print("4. Update Student Information")
    print("5. Expel Student")


if __name__ == "__main__":
    main()
