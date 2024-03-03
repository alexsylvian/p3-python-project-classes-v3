from models.__init__ import CURSOR, CONN
from models.course import Course

class Student:
    
    all = {}

    def __init__(self, name, age, course_id, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.course_id = course_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, str) and len(age):
            self._age = age
        else:
            raise ValueError(
                "age must be a non-empty string"
            )
        
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        if type(course_id) is int and Course.find_by_id(course_id):
            self._course_id = course_id
        else:
            raise ValueError(
                "course_id must reference a course in the database")
        
    