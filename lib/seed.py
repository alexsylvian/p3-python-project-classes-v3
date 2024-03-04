#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.course import Course
from models.student import Student

def seed_database():
    Student.drop_table()
    Course.drop_table()
    Course.create_table()
    Student.create_table()

    # Create seed data
    physics = Course.create("Physics", "Shlanger")
    Student.create("Lev", "43", physics.id)

seed_database()
print("Seeded database")