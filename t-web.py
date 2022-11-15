from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from database import db
#from models import Project as Project

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/my-projects')
def list_projects():
    return render_template('my-projects.html')

#@app.route('/my-projects/<project_id>')
#def get_project(project_id):
#    chosen_project = db.session.query(Project).filter_by(id=project_id).one()
#
#    return render_template('project.html', project=chosen_project)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

#@app.route()
#def view_project():
#    return render_template()

@app.route('/new-projects')
def create_project():
    return render_template('new-projects.html')

#@app.route()
#def edit_project():
#    return render_template()

#@app.route()
#def delete_project():
#    return render_template()
