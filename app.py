# app.py
import flask
from flask import Flask, request,jsonify, render_template
from flask_cors import CORS
import json
import mysql.connector
app = Flask(__name__)
app.debug = True
FLASK_APP=app
CORS(app)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root123!@#",
  database="api",
  buffered=True,
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM user")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
 if request.method == "POST":
   #print ('It Worked!')
   name = request.form['name']
   user_name = request.form['user_name']
   password = request.form['password']
   mycursor.execute("INSERT INTO user VALUES (%s,%s,%s)", (name, user_name, password))
   mydb.commit()
   mycursor.close()
   mydb.close()
   return render_template("success.html") 
   
@app.route("/empty", methods=["GET", "POST"])
def empty():
    mycursor.execute("SELECT * FROM user")
    results = mycursor.fetchall()
    print(results)
    return jsonify(results)
    mycursor.close()
    mydb.close()

@app.route("/empty.html", methods=["GET"])
def emptypage():
    return render_template("empty.html")
    mycursor.execute("SELECT * FROM user")
    results = mycursor.fetchall()
    print(results)
    return jsonify(results)
    mycursor.close()
    mydb.close()