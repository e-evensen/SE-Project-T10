from database import db

class Project(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))

    def __init__(self, title):
        self.title = title