# lib/cli.py

from helpers import (
    exit_program,
    helper_class_template,
    submenu_2
)


def main():
    while True:
        menu()
        choice = input(">> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            classes()
        elif choice == "2":
            students()
        else:
            print("Invalid choice")

def classes():
    while True:
        submenu_classes()
        choice = input(">> ")
        if choice == "0":
            break  # Go back to the main menu
        elif choice == "1":
            list_of_classes()
        elif choice == "2":
            submenu_2()
        else:
            print("Invalid choice")

def list_of_classes():
    while True:
        submenu_list_of_classes()
        choice = input(">> ")
        
        if choice == "0":
            break
        elif choice == "1":
            helper_class_template()

def students():
    pass


def menu():
    print("Please select an option:")
    print("0. Exit the Program")
    print("1. Classes Menu")
    print("2. Students Menu")

def submenu_classes():
    print("Welcome to the Classes Menu. What would you like to do?")
    print("1. List of Classes")
    print("2. Create New Class")
    print("3. Search for Class by Name")
    print("0. Go back")

def submenu_list_of_classes():
    print(f"Current Classes are 'for class in classes' CLASSSLIST GOES HERE.") 
    print("Please Select a Class")
    print("for class in classes print etc")
    print("0: Go Back")
    print("1. TEMPLATE: PHYSICS")

def submenu_class_template():
    print("Welcome to x Class. What would you like to do?")
    print("0. Go Back")
    print("1. List of Students in this Class")
    print("2. Update Class Name or Teacher")
    print("3. Add Student to Class")
    print("4. Delete Class")

def sumbenu_students():
    print("Welcome to the Students Menu. What would you like to do?")
    print("0. Go Back")
    print("1. List of Students")
    print("2. Search for Student by Name")
    print("3. Add New Student")
    print("4. Update Student Information")
    print("5. Expel Student")


if __name__ == "__main__":
    main()
