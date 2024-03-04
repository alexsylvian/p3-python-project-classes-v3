# lib/helpers.py
from models.course import Course
from models.student import Student

def submenu_2():
    print("Performing Submenu Option 2")

def helper_course_template():
    print("course is PHYSICS. TEACHER is LOL")

def exit_program():
    print("Exiting the program.")
    exit()

def list_courses():
    print("it is running")
    # courses = Course.get_all()
    # for course in courses:
    #     print(course)

def find_student_by_name():
    print("love")
    name = input("Enter the student's name: ")
    student = Student.find_by_name(name)
    print(student) if student else print(
        f'Student {name} not found')
    
def create_new_course():
    subject = input("Enter the course's subject: ")
    teacher = input("Enter the course's teacher: ")
    try:
        course = Course.create(subject, teacher)
        print(f'Success: {course}')
    except Exception as exc:
        print("Error creating course: ", exc)

def create_initial_table():
    Course.create_table()

