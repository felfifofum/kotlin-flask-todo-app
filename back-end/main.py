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
    id = db.Column(db.Integer, primary_key = True) 
    todoitem = db.Column("todoitem", db.String(200))
    complete = db.Column(db.Boolean)

    def __init__(self,todoitem):
        self.todoitem = todoitem


@app.route('/')
def index():
    return render_template("../front-end/app/src/java/com/example/todolist/MainActivity.kt")


@app.route("/add", methods=["POST"])
def add():
    if request.method == 'POST':
        #check content on todolist
        new_item = Todo()
    try:
        db.session.add(Todo)
        db.session.commit()
        return redirect('/')
    except:
        return 'there was an error adding an item'
    
    
@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id))
    todo.complete = True
    db.session.commit()

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    task_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect('/')
        todo = request.form["sample"] #find part in kotlin
    except:
        return "there is a problem deleting that task"


#initiate flask framework
if __name__ == "__main__":
    app.run(debug=True)

