from models.__init__ import CURSOR, CONN
from models.course import Course

class Student:
    
    all = {}

    def __init__(self, name, age, course_id=None, id=None):
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
        if isinstance(age, (int, str)) and (isinstance(age, str) and len(age) or isinstance(age, int)):
            self._age = age
        else:
            raise ValueError("Age must be a non-empty string or an integer")
        
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        if course_id is None or (isinstance(course_id, int)):
            self._course_id = course_id
        else:
            raise ValueError("course_id must reference an existing course in the database or be None")
        
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

    @classmethod
    def create(cls, name, age, course_id):
        """ Initialize a new Student instance and save the object to the database """
        student = cls(name, age, course_id)
        student.save()
        return student

    @classmethod
    def instance_from_db(cls, row):
        """Return a Student object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        student = cls.all.get(row[0])
        if student:
            # ensure attributes match row values in case local instance was modified
            student.name = row[1]
            student.age = row[2]
            student.course_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            student = cls(row[1], row[2], row[3])
            student.id = row[0]
            cls.all[student.id] = student
        return student
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Student object per table row"""
        sql = """
            SELECT *
            FROM students
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """Return Student object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM students
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
