from database import db
import datetime
import datetime

class Project(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    projName = db.Column("projName", db.String(200))
    projDesc = db.Column("projDesc", db.String(500))
    createDate = db.Column("createDate", db.String(50))
    dueDate = db.Column("dueDate", db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, projName, projDesc, createDate, dueDate, user_id):
        self.projName = projName
        self.projDesc = projDesc
        self.createDate = createDate
        self.dueDate = dueDate
        self.user_id = user_id

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    projects = db.relationship("Project", backref="user", lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()
