from flask import render_template, request, redirect, url_for
from app import app
#from app.models import Todo
from app import db

@app.route('/')
def hello():
    return 'this is the home page'

@app.route("/add", methods=["POST"])
def debug():
    todo = request.form["sample"]
    print(todo)
    return "added"
    db.session.add(todo)
    db.session.commit()

@app.route("/delete", methods=["POST"])
def debug():
    todo = request.form["sample"]
    print(todo)
    return "deleted"
    db.session.delete(todo)
    db.session.commit()