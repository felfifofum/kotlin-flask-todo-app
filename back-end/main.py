from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
#import app
#from app import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

file_path = os.path.abspath(os.getcwd())+"/todolist.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "to-do"

    id = db.Column("id", db.integer, primary_key = True)
    todoitem = db.Column("todoitem", db.String(200))

    def __init__(self,todoitem):
        self.todoitem = todoitem


@app.route('/', methods=['POST','GET'])
def home():
    return render_template("../front-end/app/src/java/com/example/todolist/MainActivity.kt")
    return "its working!"


@app.route("/add", methods=["POST"])
def home():
    db.session.add(Todo)
    db.session.commit()
    Todo = request.form["sample"]
    return "added"
    

    return redirect (url_for('/'))

@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id))
    Todo.complete = True
    db.session.commit()

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    task_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_delete)
        db.session.commit()
        todo = request.form["sample"] #find part in kotlin
    except:
        return "there is a problem deleting that task"


#initiate flask framework
if __name__ == "__main__":
    app.run(debug=True)

