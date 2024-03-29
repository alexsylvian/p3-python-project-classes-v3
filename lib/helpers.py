# lib/helpers.py
from models.course import Course
from models.student import Student

def exit_program():
    print("Exiting the program.")
    exit()

def create_initial_table():
    Course.create_table()

def create_new_course():
    subject = input("Enter the course's subject: ")
    teacher = input("Enter the course's teacher: ")
    try:
        course = Course.create(subject, teacher)
        print(f'Success: {course.subject} course created')
    except Exception as exc:
        print("Error creating course: ", exc)

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
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course.subject} - {course.teacher}")

        selected_id = input("Enter the course # to view details (0 to go back): ")
        if selected_id == "0":
            break

        try:
            selected_id = int(selected_id)
            if 1 <= selected_id <= len(courses):
                selected_course = courses[selected_id - 1]
                navigate_course(selected_course)
            else:
                print("Invalid Choice. Please Select a Number on the List of Courses")
        except ValueError:
            print("Invalid Choice")

def find_course_by_id(course_id):
    for course in Course.get_all():
        if course.id == course_id:
            return course
    return None

def navigate_course(course):
    while True:
        print(f"Welcome to the {course.subject} course, taught by {course.teacher}. What would you like to do?")
        print("0. Go Back")
        print("1. See List of Students")
        print("2. Update Course Information")
        print("3. Create New Student and Add to Course")
        print("4. Add Enrolled Student to Course")
        print("5. Remove Student from Course")
        print("6. Delete Course")
        choice = input(">> ")

        if choice == "0":
            break
        elif choice == "1":
            list_students_in_course(course)
        elif choice == "2":
            update_course_details(course)
        elif choice == "3":
            create_and_add_student_to__selected_course(course)
        elif choice == "4":
            add_student_to_course(course)
        elif choice == "5":
            remove_student_from_course(course)
        elif choice == "6":
            delete_course(course)
            list_courses()
        else:
            print("Invalid Choice")

def list_students_in_course(course):
    students = course.students()
    print(f"Students in {course.subject}:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student.name} - {student.age}")

def update_course_details(course):
    print(f"Current details: {course.subject} - {course.teacher}")
    new_subject = input("Enter the new subject (leave blank to keep current): ")
    new_teacher = input("Enter the new teacher (leave blank to keep current): ")

    if new_subject or new_teacher:
        course.subject = new_subject or course.subject
        course.teacher = new_teacher or course.teacher
        course.update()
        print(f"Course details updated: {course.subject} - {course.teacher}")
    else:
        print("No changes made.")

def create_and_add_new_student():
    print("Creating a new student:")
    name = input("Enter the student's name: ")
    while True:
        age_input = input("Enter the student's age: ")
        if age_input.isdigit():
            age = age_input
            break
        else:
            print("Invalid input. Please enter a valid age as a number.")

    courses = Course.get_all()
    print("Available courses:")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course.subject} - {course.teacher}")

    selected_course_index = int(input("Enter the course number to enroll the student (0 for none): ")) - 1

    if selected_course_index == -1:
        course_id = None
    elif 0 <= selected_course_index < len(courses):
        course_id = courses[selected_course_index].id
    else:
        print("Invalid course selection. Student will not be enrolled.")
        return

    try:
        student = Student.create(name, age, course_id)
        print(f"Success: {student.name} has been enrolled in the course.")
    except Exception as exc:
        print("Error creating student: ", exc)

def create_and_add_student_to__selected_course(course):
    print("Creating and adding a new student to the course.")

    student_name = input("Enter the student's name: ")
    
    while True:
        age_input = input("Enter the student's age: ")
        if age_input.isdigit():
            student_age = int(age_input)
            break
        else:
            print("Invalid input. Please enter a valid age as a number.")

    try:
        student = Student.create(student_name, student_age, course_id=course.id)
        print(f"Success: {student.name} has been added to {course.subject} course.")
    except Exception as exc:
        print(f"Error creating student: {exc}")

def add_student_to_course(course):
    print("Adding a student to the course.")

    student_name = input("Enter the student's name: ")

    student = Student.find_by_name(student_name)

    if student:
        student.course_id = course.id

        try:
            student.update()
            print(f'Successfully added {student_name} to {course.subject} course.')
        except Exception as exc:
            print(f"Error updating student information: {exc}")
    else:
        print(f"Student {student_name} not found.")

def remove_student_from_course(course):
    print("Removing a student from the course.")

    student_name = input("Enter the student's name: ")

    student = Student.find_by_name(student_name)

    if student:
        student.course_id = None

        try:
            student.update()
            print(f'Successfully removed {student_name} from {course.subject} course.')
        except Exception as exc:
            print(f"Error updating student information: {exc}")
    else:
        print(f"Student {student_name} not found.")

def delete_course(course):
    confirmation = input(f"Are you sure you want to delete {course.subject} (Y/N)? ").strip().lower()

    if confirmation == "y":
        course.delete()
        print(f"{course.subject} course deleted.")
    else:
        print("Deletion canceled.")

#################
        
def create_initial__student_table():
    Student.create_table()

def list_of_students():
    students = Student.get_all()
    for student in students:
        if student.course_id is not None:
            course_subject = Course.find_by_id(student.course_id).subject
            print(f"{student.name}, age {student.age}, in {course_subject} course")
        else:
            print(f"{student.name}, age {student.age}, not currently enrolled in a course")
        
def find_student_by_name():
    name = input("Enter the student's name: ")
    student = Student.find_by_name(name)

    if student:
        if student.course_id is not None:
            course_subject = Course.find_by_id(student.course_id).subject
            print(f"{student.name}, age {student.age}, in {course_subject} course")
        else:
            print(f"{student.name}, age {student.age}, not currently enrolled in a course")
    else:
        print(f'Student {name} not found')
        
def create_new_student():
    print("Creating a new student:")
    name = input("Enter the student's name: ")
    while True:
        age_input = input("Enter the student's age: ")
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Invalid input. Please enter a valid age as a number.")

    try:
        student = Student.create(name, age, course_id=None)
        print(f"Success: Welcome, {student.name}")
    except Exception as exc:
        print("Error creating student: ", exc)

def update_student_information():
    print("Updating student information.")

    student_name = input("Enter the student's name: ")

    student = Student.find_by_name(student_name)

    if student:
        updated_name = input(f"Enter the updated name for {student_name} (press Enter to keep the same): ")
        updated_age = input(f"Enter the updated age for {student_name} (press Enter to keep the same): ")

        if updated_name:
            student.name = updated_name
        if updated_age:
            student.age = updated_age

        try:
            student.update()
            print(f'Successfully updated information for {student_name}.')
        except Exception as exc:
            print(f"Error updating student information: {exc}")
    else:
        print(f"Student {student_name} not found.")

def expel_student():
    name = input("Enter the student's name to expel: ")
    student = Student.find_by_name(name)

    if student:
        confirmation = input(f"Are you sure you want to expel {name}? (y/n): ").lower()

        if confirmation == 'y':
            student.delete()
            print(f"Student {name} has been expelled.")
        else:
            print(f"Expulsion of {name} canceled.")
    else:
        print(f'Student {name} not found.')