from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import login_manager
from app import db

class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	firstname = db.Column(db.String(50),nullable = True)
	lastname = db.Column(db.String(50),nullable = True)
	email = db.Column(db.String(50),nullable = True)
	username = db.Column(db.String(64),nullable = True)
	password = db.Column(db.String(100),nullable = True)
	password_hash = db.Column(db.String(128), nullable = True)

	def __repr__(self):
		return "<User %s>" % self.firstname

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	#Used for generating hashes of passwords	
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	#Verification of password n database
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))