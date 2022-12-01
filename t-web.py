from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from forms import LoginForm
from forms import RegisterForm
from forms import CommentForm
from datetime import datetime
from datetime import timedelta
from database import db
from models import Project as Project
from models import User as User
from models import Comment as Comment

import bcrypt

# from models import Project as Project

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///t-web_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'TWEBISSAFE'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/index')
def index():
    if session.get('user'):
        return render_template('index.html', user=session['user'])
    return render_template('index.html')


@app.route('/my-projects')
def list_projects():
    if session.get('user'):
        projects = db.session.query(Project).filter_by(user_id=session['user_id']).all()
        return render_template('my-projects.html', user=session['user'], projects=projects)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # validate_on_submit only validates using POST
    if login_form.validate_on_submit():
        # we know user exists. We can use one()
        the_user = db.session.query(User).filter_by(email=request.form['email']).one()
        # user exists check password entered matches stored password
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            # password match add user info to session
            session['user'] = the_user.first_name
            session['user_id'] = the_user.id
            # render view
            return redirect(url_for('list_projects'))

        # password check failed
        # set error message to alert user
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    if session.get('user'):
        session.clear()

    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        new_user = User(first_name, last_name, request.form['email'], h_password)
        db.session.add(new_user)
        db.session.commit()
        session['user'] = first_name
        session['user_id'] = new_user.id
        return redirect(url_for('list_projects'))

    return render_template('register.html', form=form)


@app.route('/my-projects/<project_id>/comment', methods=['POST'])
def new_comment(project_id):
    if session.get('user'):
        comment_form = CommentForm()
        # validate_on_submit only validates using POST
        if comment_form.validate_on_submit():
            # get comment data
            comment_text = request.form['comment']
            today = datetime.now()
            today = today.strftime("%m-%d-%Y")
            new_record = Comment(today, comment_text, int(project_id), session['user_id'], session['user'])
            db.session.add(new_record)
            db.session.commit()

        return redirect(url_for('view_project', project_id=project_id, user=session['user']))

    else:
        return redirect(url_for('login'))


@app.route('/my-projects/<project_id>')
def view_project(project_id):
    if session.get('user'):
        # a_user = db.session.query(User).filter_by(email='admin@gmail.com').one()
        project = db.session.query(Project).filter_by(id=project_id, user_id=session['user_id']).one()
        form = CommentForm()
        return render_template('project.html', project=project, user=session['user'], form=form)
    else:
        return redirect(url_for('login'))


@app.route('/new-projects', methods=['GET', 'POST'])
def create_project():
    if session.get('user'):
        if request.method == 'POST':
            projName = request.form['project-name']
            projDesc = request.form['project-desc']
            today = datetime.now()
            due = today + timedelta(days=7)
            today = today.strftime("%m-%d-%Y")
            due = due.strftime("%m-%d-%Y")

            new_project = Project(projName, projDesc, today, due, session['user_id'])
            db.session.add(new_project)
            db.session.commit()

            return redirect(url_for('list_projects'))
        else:
            return render_template('new-projects.html', user=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/my-projects/edit/<project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    if session.get('user'):
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
            return render_template('new-projects.html', user=session['user'], project=project)
    else:
        return redirect(url_for('login'))


@app.route('/my-projects/delete/<project_id>', methods=['POST'])
def delete_project(project_id):
    if session.get('user'):
        project = db.session.query(Project).filter_by(id=project_id).one()
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for('list_projects'))
    else:
        return redirect(url_for('login'))

@app.route('/my-projects/share/<project_id>', methods=['POST'])
def share_project(project_id):
    return redirect(url_for('index'))

