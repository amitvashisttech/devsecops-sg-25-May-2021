from flask import Flask, render_template, request, redirect
# Adding Databases Info.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Intial App
app = Flask(__name__)

# Intial Databases.
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


@app.route("/", methods=['GET', 'POST'])
def home():
     if request.method == 'POST': 
          title = request.form['title']
          desc  = request.form['desc']
          todo = Todo(title=title, desc=desc)
          db.session.add(todo)
          db.session.commit()

     allTodo = Todo.query.all()
     return render_template('index.html',allTodo=allTodo)


@app.route("/show")
def product():
     allTodo = Todo.query.all()
     print(allTodo)
     return "Sample Project"

if __name__ == '__main__':
   app.run('0.0.0.0',8090)
