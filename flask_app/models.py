from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Person {self.name} from {self.place}, {self.city}>"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_class = db.Column(db.String(50), nullable=False)
    school_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.name} from {self.school_name} Class: {self.student_class}>"
