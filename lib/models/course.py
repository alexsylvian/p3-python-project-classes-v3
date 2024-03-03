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
            name TEXT,
            location TEXT)
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