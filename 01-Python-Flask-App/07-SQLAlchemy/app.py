# Basic Flask App 
# Initalize Flask From Flask Module

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initalize Flask as App
app = Flask(__name__)


# Intialize SQL Databases.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
     sno = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(200), nullable=False)
     desc = db.Column(db.String(500), nullable=False)
     date_created = db.Column(db.DateTime, default=datetime.utcnow)

     #def __repr__(self) -> str:
     #    return f"{self.sno} - {self.title}"
     def __repr__(self):
         #return f"{self.sno} - {self.title}"
         #return '%r %s' % self.sno self.title
         return "Pair({}, {})".format(self.sno, self.title)


@app.route("/")
def home():
    todo = Todo(title="First Todo", desc="My Todo Test")
    db.session.add(todo)
    db.session.commit()
    allTodo  = Todo.query.all()
    return render_template('index.html',allTodo=allTodo)


@app.route("/show")
def product():
    allTodo  = Todo.query.all()
    print(allTodo)
    return "Sample Project"

if __name__ == '__main__':
   app.run('0.0.0.0',8080)

