from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "to-do"

id = db.Column(db.integer, primary_key = True)
todoitem = db.Column(db.String(100))

def __init__(self, todoitem):
    self.todoitem = todoitem