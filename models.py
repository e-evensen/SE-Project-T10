from database import db
import datetime

class Project(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    projName = db.Column("project-name", db.String(200))
    projDesc = db.Column("project-desc", db.String(500))
    createDate = db.Column("date-created", db.datetime)
    dueDate = db.Column("date-due", db.datetime)
    members = db.Column("members", db.list)

    def __init__(self, projName, projDesc, createDate, dueDate):
        self.projName = projName
        self.projDesc = projDesc
        self.createDate = createDate
        self.dueDate = dueDate

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password