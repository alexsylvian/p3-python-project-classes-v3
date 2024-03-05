from models.__init__ import CURSOR, CONN

class Course:
    
    all = {}

    def __init__(self, subject, teacher, id=None):
        self.id = id
        self.subject = subject
        self.teacher = teacher
    
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if isinstance(subject, str) and len(subject):
            self._subject = subject
        else:
            raise ValueError(
                "subject must be a non-empty string"
            )
        
    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        if isinstance(teacher, str) and len(teacher):
            self._teacher = teacher
        else:
            raise ValueError(
                "Teacher must be a non-empty string"
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Course instances """
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            subject TEXT,
            teacher TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Course instances """
        sql = """
            DROP TABLE IF EXISTS courses;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the subject and teacher values of the current Course instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO courses (subject, teacher)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.subject, self.teacher))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, subject, teacher):
        """ Initialize a new Course instance and save the object to the database """
        course = cls(subject, teacher)
        course.save()
        return course

    def update(self):
        """Update the table row corresponding to the current Course instance."""
        sql = """
            UPDATE courses
            SET subject = ?, teacher = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.subject, self.teacher, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Course instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM courses
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Course object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        course = cls.all.get(row[0])
        if course:
            # ensure attributes match row values in case local instance was modified
            course.subject = row[1]
            course.teacher = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            course = cls(row[1], row[2])
            course.id = row[0]
            cls.all[course.id] = course
        return course
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Course object per row in the table"""
        sql = """
            SELECT *
            FROM courses
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_subject(cls, subject):
        """Return a Course object corresponding to first table row matching specified subject"""
        sql = """
            SELECT *
            FROM courses
            WHERE subject is ?
        """

        row = CURSOR.execute(sql, (subject,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def students(self):
        """Return list of students associated with current course"""
        from models.student import Student
        sql = """
            SELECT * FROM students
            WHERE course_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Student.instance_from_db(row) for row in rows
        ]