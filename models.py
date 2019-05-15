from server import db

class Repo(db.Model):
    __tablename__ = 'repos'

    id = db.Column(db.Integer, primary_key=True)
    gitid = db.Column(db.Integer)
    name = db.Column(db.String())
    owner = db.Column(db.String())
    chats = db.Column(db.String())

    def __init__(self, name, owner, chats):
        self.name = name
        self.owner = owner
        self.chats = chats

    def __repr__(self):
        return '<id {}>'.format(self.id)
