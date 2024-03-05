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
        print(f'Success: {course.subject} course created')
    except Exception as exc:
        print("Error creating course: ", exc)

def create_initial_table():
    Course.create_table()

def create_course_list():
    courses = Course.get_all()
    for course in courses:
        print(course.subject)

def find_course_by_subject():
    subject = input("Enter the course's subject: ")
    course = Course.find_by_subject(subject)
    print(course.subject + ', ' + course.teacher) if course else print(
        f'Course {subject} not found')
    
def list_courses():
    courses = Course.get_all()

    while True:
        print("Current courses:")
        for course in courses:
            print(f"{course.id}: {course.subject} - {course.teacher}")

        selected_id = input("Enter the course # to view details (0 to go back): ")
        if selected_id == "0":
            break

        # selected_course = find_course_by_id(int(selected_id))
        # if selected_course:
        #     navigate_course(selected_course)
