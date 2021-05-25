# Basic Flask App 
# Initalize Flask From Flask Module

from flask import Flask

# Initalize Flask as App
app = Flask(__name__)


@app.route("/")
def home():
  return "Welcome to the Basics of Flask App"


@app.route("/hello")
def home_world():
  return "Hello World"


@app.route("/amit")
def home_amit():
  return "Hey Amit"


@app.route("/guest/<guest>")
def home_guest(guest):
  return "Hello %s as Guest" % guest

app.run('0.0.0.0',8080)

