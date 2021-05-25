# Basic Flask App 
# Initalize Flask From Flask Module

from flask import Flask, render_template

# Initalize Flask as App
app = Flask(__name__)


@app.route("/")
def home():
  return render_template('index.html')

app.run('0.0.0.0',8080)

