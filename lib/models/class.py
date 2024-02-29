from models.__init__ import CURSOR, CONN

class Class:
    
    all = {}

    def __init__(self, subject, teacher, id=None):
        self.id = id
        self.subject = subject
        self.teacher = teacher

    def __repr__(self):
        return f"<Department {self.id}: {self.subject}, {self.teacher}>"
    
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