# Basic Flask App 
# Initalize Flask From Flask Module

from flask import Flask

# Initalize Flask as App
app = Flask(__name__)


@app.route("/")
def home():
  return "Hello World!"

app.run('0.0.0.0',8080)

