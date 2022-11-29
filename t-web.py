from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from forms import LoginForm
from datetime import datetime
from datetime import timedelta
from database import db
from models import Project as Project
from models import User as User
#from models import Project as Project

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///t-web_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/my-projects')
def list_projects():
    a_user =  db.session.query(User).filter_by(email='admin@gmail.com')
    projects = db.session.query(Project).all()

    return render_template('my-projects.html', user = a_user, projects = projects)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    if session.get('user'):
        session.clear()

    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/my-projects/<project_id>')
def view_project(project_id):
    #a_user = db.session.query(User).filter_by(email='admin@gmail.com').one()
    project = db.session.query(Project).filter_by(id=project_id).one()

    return render_template('project.html', project=project)

@app.route('/new-projects', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        projName = request.form['project-name']
        projDesc = request.form['project-desc']
        today = datetime.now()
        due = today + timedelta(days=7)
        today = today.strftime("%m-%d-%Y")
        due = due.strftime("%m-%d-%Y")

        new_project = Project(projName, projDesc, today, due)
        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for('list_projects'))
    else:
        return render_template('new-projects.html')

@app.route('/my-projects/edit/<project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    if request.method == 'POST':
        projName = request.form['project-name']
        projDesc = request.form['project-desc']
        project = db.session.query(Project).filter_by(id=project_id).one()
        project.projName = projName
        project.projDesc = projDesc
        db.session.add(project)
        db.session.commit()

        return redirect(url_for('list_projects'))

    else:
        project = db.session.query(Project).filter_by(id=project_id).one()
        return render_template('new-projects.html', project=project)


@app.route('/my-projects/delete/<project_id>', methods=['POST'])
def delete_project(project_id):
    project = db.session.query(Project).filter_by(id=project_id).one()
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('list_projects'))
