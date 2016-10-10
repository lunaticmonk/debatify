from werkzeug.security import generate_password_hash, check_password_hash
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
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
	confirmed = db.Column(db.Boolean, default = False)
	question = db.relationship("Question", backref = "owner", lazy = 'dynamic')

	def __repr__(self):
		return "<User %s>" % self.firstname

	#Related to werkzeug security

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

	# def generate_confirmation_token(self, expiration = 120):
	# 	s = Serializer(app.config['SERIAL_KEY'],expiration)
	# 	return s.dumps({'confirm' : self.id})

	# def confirm(self, token):
	# 	s = Serializer(current_app.config['SECRET_KEY'])
	# 	try:
	# 		data = s.loads(token)
	# 	except:
	# 		return False
	# 	if data.get('confirm') != self.id:
	# 		return False
	# 	self.confirmed = True
	# 	db.session.add(self)
	# 	return True

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


# Another table containing questions of users

class Question(db.Model):
	__tablename__ = "questions"
	id = db.Column(db.Integer, primary_key = True)
	questions = db.Column(db.String(500))
	topic = db.Column(db.String(500))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))