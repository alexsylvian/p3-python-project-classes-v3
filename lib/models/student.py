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
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Student instances """
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age TEXT,
            course_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Student instances """
        sql = """
            DROP TABLE IF EXISTS students;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, age, and course id values of the current Student object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO students (name, age, course_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.course_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Student instance."""
        sql = """
            UPDATE students
            SET name = ?, age = ?, course_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age,
                             self.course_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Student instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM students
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None