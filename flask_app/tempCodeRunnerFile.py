from flask import Flask, render_template, request, redirect, url_for

import pymysql

app = Flask(__name__)

# Configure database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Devansh%40123@localhost/mysql_server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import db and models
from models import db, Person, Student

# Initialize SQLAlchemy with app
db.init_app(app)

# Create database if it doesn't exist
host = 'localhost'
user = 'root'
password = 'Devansh@123'
database_name = 'mysql_server'

connection = pymysql.connect(host=host, user=user, password=password)
connection.autocommit(True)
try:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' ensured to exist.")
finally:
    connection.close()

@app.before_request
def create_tables_and_seed():
    with app.app_context():
        db.create_all()
        if Person.query.first() is None:
            sample_persons = [
                Person(name='Alice', place='Park', city='New York'),
                Person(name='Bob', place='Museum', city='Chicago'),
                Person(name='Charlie', place='Library', city='San Francisco'),
                Person(name='Diana', place='Cafe', city='Boston'),
                Person(name='Eve', place='Zoo', city='Seattle')
            ]
            db.session.bulk_save_objects(sample_persons)

        if Student.query.first() is None:
            sample_students = [
                Student(name='John', student_class='5th', school_name='XYZ'),
                Student(name='Emma', student_class='6th', school_name='XYZ'),
                Student(name='Liam', student_class='5th', school_name='XYZ'),
                Student(name='Olivia', student_class='7th', school_name='XYZ'),
                Student(name='Noah', student_class='6th', school_name='XYZ')
            ]
            db.session.bulk_save_objects(sample_students)

        db.session.commit()

@app.route("/", methods=["GET"])
def home():
    # Show login page
    return render_template('sign_in.html')

@app.route("/login", methods=["POST"])
def login():
    # Read form data
    email_or_username = request.form.get('email_or_username')
    password = request.form.get('password')
    user_role = request.form.get('user_role')
    preferred_district = request.form.get('preferred_district')
    remember_me = request.form.get('remember_me')

    # TODO: Integrate real authentication here,
    # For demo, accept any input and redirect
    return redirect(url_for('landing'))

@app.route("/landing")
def landing():
    # Simple landing page after login
    return render_template('landing_page.html')

@app.route("/students")
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
