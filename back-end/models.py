from flask_sqlalchemy import SQLAlchemy
from app import db

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "to-do"

id = db.Column("id", db.integer, primary_key = True)
todoitem = db.Column("todoitem", db.String(200))


def __init__(self,todoitem):
    self.todoitem = todoitem