# lib/helpers.py

def submenu():
    print("Welcome to the Classes Menu. What Would You Like to do?")
    print("1. List of Classes")
    print("2. Create New Class")
    print("3. Search for Class by Name")
    print("0. Go back")

def submenu_physics():
    print("Welcome to Physics Class. What would you like to do?")
    print("0. Go Back")

def helper_physics():
    while True:
        submenu_physics()
        submenu_physics_choice = input(">> ")
        print("Welcome to Physics Class. What would you like to do?")
        print("0. Go Back")
        
        if submenu_physics_choice == "0":
            break


def helper_submenu_2():
    print("Performing Submenu Option 2")

def classes():
    while True:
        submenu()
        submenu_choice = input(">> ")

        if submenu_choice == "0":
            break  # Go back to the main menu
        elif submenu_choice == "1":
            helper_physics()
        elif submenu_choice == "2":
            helper_submenu_2()
        else:
            print("Invalid choice")

def students():
    pass

def exit_program():
    print("Exiting the program.")
    exit()
