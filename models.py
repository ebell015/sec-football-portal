from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    logo_url = db.Column(db.String(255), nullable=True)
    players = db.relationship('Player', backref='team')

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(20))
    nil_value = db.Column(db.Float)
    depth = db.Column(db.Integer, default=1)  # 👈 NEW FIELD
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))


