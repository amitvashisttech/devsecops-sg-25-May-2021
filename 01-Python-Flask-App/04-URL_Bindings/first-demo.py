# Basic Flask App 
# Initalize Flask From Flask Module

from flask import Flask, redirect, url_for

# Initalize Flask as App
app = Flask(__name__)


@app.route("/")
def home():
  return "Welcome to the Basics of Flask App"


@app.route("/admin")
def home_admin():
  return "Hey Admin - How are you doing today?"


@app.route("/amit")
def home_amit():
  return "Hey Amit"


@app.route("/guest/<guest>")
def home_guest(guest):
  return "Hello %s as Guest" % guest

@app.route("/user/<name>")
def home_user(name):
    if name == 'admin':
       return redirect(url_for('home_admin'))
    else:
       return redirect(url_for('home_guest', guest = name ))



app.run('0.0.0.0',8080)

