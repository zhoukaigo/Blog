from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.login import LoginManager, UserMixin
from . import db, login_manager

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	social_id = db.Column(db.String(64), nullable=False, unique=True)
	nickname = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(64), nullable=True)