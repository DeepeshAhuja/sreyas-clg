from flask import Flask, render_template, request, redirect,session,flash
from flask_mysqldb import MySQLdb,MySQL
import MySQLdb.cursors
from flask_session import Session
from flask_mail import Mail, Message
import datetime

app= Flask(__name__)
app.secret_key = 'abcdefg123'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root123$'
app.config['MYSQL_DB']='university_database'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

mysql=MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return render_template("about.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/department')
def department():
    return render_template("department.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/cse')
def cse():
    return render_template("cse.html")

@app.route('/aiml')
def aiml():
    return render_template("aiml.html")

@app.route('/ds')
def ds():
    return render_template("ds.html")

@app.route('/student')
def student():
    return render_template("student.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)
