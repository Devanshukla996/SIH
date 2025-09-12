
from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
load_dotenv()  

import pymysql

app = Flask(__name__)



# Configure database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import db and models
# from models import db, Person, Student

# Initialize SQLAlchemy with app
# db.init_app(app)

# Create database if it doesn't exist
host = 'localhost'
user = 'root'
password = 'Devansh@123'
database_name = 'mysql_server'

# connection = pymysql.connect(host=host, user=user, password=password)
# connection.autocommit(True)
# try:
#     with connection.cursor() as cursor:
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
#         print(f"Database '{database_name}' ensured to exist.")
# finally:
#     connection.close()

# @app.before_request
# def create_tables_and_seed():
#     with app.app_context():
#         db.create_all()
  

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





@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/railway')
def railways():
    return render_template('railway.html')

@app.route("/bus")
def Bus():
    return render_template('bus.html', )




@app.route("/shopping")
def Shopping():
    return render_template('market.html',)

@app.route("/handicrafts")
def Handicrafts():
    return render_template('tribal_handicraft_copy.html',)

@app.route("/location")
def Location():
    return render_template('index.html',)

@app.route("/sohrai")
def sohrai():
    return render_template("sohrai.html")

@app.route("/khovar")
def khovar():
    return render_template("khovar.html")

@app.route("/dhokra")
def dhokra():
    return render_template("dhokra.html")

@app.route("/bamboo_tokri")
def bamboo_tokri():
    return render_template("bamboo_tokri.html")

@app.route("/paitkar")
def paitkar():
    return render_template("paitkar.html")

@app.route("/ecotourism")
def ecotourism():
    return render_template("ecotourism1.html")

@app.route("/events")
def events():
    return render_template("events.html")



@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/koderma")
def Koderma():
    return render_template('koderma1.html',)



@app.route("/ranchi")
def Ranchi():
    return render_template('ranchi.html',)

@app.route("/jamshedpur")
def Jamshedpur():
    return render_template('jamshedpur.html',)

@app.route("/gumla")
def Gumla():
    return render_template('gumla.html',)

@app.route("/deoghar")
def Deoghar():
    return render_template('deoghar.html',)


@app.route("/login")
def Login():
    return render_template('login.html',) 

@app.route("/profile")
def Profile ():
    return render_template('profile.html',)

 
@app.route("/bokaro")
def Bokaro():
    return render_template('bokaro.html',)

@app.route("/ramgarh")
def Ramgarh():
    return render_template('ramgarh.html',)

@app.route("/latehar")
def Latehar():
    return render_template('latehar.html',)

@app.route("/airport")
def airport():
    return render_template('airport.html', )

@app.route("/help")
def Helpus():
    return render_template('helpus.html', )

@app.route("/help_me")
def Help():
    return render_template("excuse.html",)


@app.route("/bestseller")
def Bestseller():
    return render_template("bestseller.html")




@app.route("/sohrai_festival")
def sohrai_festival():
    return render_template(" sorhai_festival.html")

@app.route("/karma_festival")
def karma_festival():
    return render_template("karam.html")

@app.route("/sarhul_festival")
def sarhul_festival():
    return render_template("sarhul1.html")

@app.route("/chhath_puja")
def chhath_puja():
    return render_template("chhath.html")

@app.route("/tusu_parab")
def tusu_parab():
    return render_template("tusu1.html")

@app.route("/dashboard")
def Dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
