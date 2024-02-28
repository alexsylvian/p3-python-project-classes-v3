# lib/cli.py

from helpers import (
    exit_program,
    submenu,
    helper_physics,
    helper_submenu_2
)


def main():
    while True:
        menu()
        choice = input("> ")
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


def menu():
    print("Please select an option:")
    print("0. Exit the Program")
    print("1. Classes Menu")
    print("2. Students Menu")


if __name__ == "__main__":
    main()
