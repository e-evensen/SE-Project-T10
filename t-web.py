from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/my-projects')
def list_projects():
    return 1

@app.route()
def view_project():
    return 1

@app.route('new-projects')
def create_project():
    return 1

@app.route()
def edit_project():
    return 1

@app.route()
def delete_project():
    return 1
