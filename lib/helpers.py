# lib/helpers.py
from models.course import Course

def submenu_2():
    print("Performing Submenu Option 2")

def helper_course_template():
    print("course is PHYSICS. TEACHER is LOL")

def exit_program():
    print("Exiting the program.")
    exit()

def list_courses():
    courses = Course.get_all()
    for course in courses:
        print(course)

