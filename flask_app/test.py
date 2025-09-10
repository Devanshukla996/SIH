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
  

@app.route("/", methods=["GET"])
def home():
    # Show login page
    return render_template('landing_page.html')

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

    return redirect(url_for('dashboard'))



@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/railway')
def railways():
    return render_template('railway.html')

@app.route("/bus")
def Bus():
    return render_template('bus.html', )


@app.route("/help")
def Helpus():
    return render_template('helpus.html', )

@app.route("/airport")
def airport():
    return render_template('airport.html', )
if __name__ == "__main__":
    app.run(debug=True)
