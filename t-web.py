from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
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

@app.route('/new-projects', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        projName = request.form['projName']
        projDesc = request.form['projDesc']
        today = datetime.datetime.now()
        due = today + timedelta(days=7)
        today = today.strftime("%m-%d-%Y")
        due = due.strftime("%m-%d-%Y")

        new_project = Project(projName, projDesc, today, due)

        return redirect(url_for('my-projects'))
    else:
        return render_template('new-projects.html')

#@app.route()
#def edit_project():
#    return render_template()

#@app.route()
#def delete_project():
#    return render_template()
