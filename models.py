from database import db

class Project(db.model):
    title = 'temp'

    def __init__(self, title):
        self.title = title