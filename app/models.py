from werkzeug.security import generate_password_hash, check_password_hash
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin,AnonymousUserMixin
from app import login_manager
from app import db
from datetime import datetime

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
	location = db.Column(db.String(64),nullable = True)
	about_me = db.Column(db.Text(),nullable = True)
	member_since = db.Column(db.DateTime(), default=datetime.utcnow,nullable = True)
	last_seen = db.Column(db.DateTime(), default=datetime.utcnow,nullable = True)
	#role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def ping(self):
		self.last_seen = datetime.utcnow()
		db.session.add(self)

	# def __init__(self, **kwargs):
	# 	super(User, self).__init__(**kwargs)
	# 	if self.role is None:
	# 		if self.email == current_app.config['FLASKY_ADMIN']:
	# 			self.role = Role.query.filter_by(permissions=0xff).first()
	# 		if self.role is None:
	# 			self.role = Role.query.filter_by(default=True).first()

	# def __repr__(self):
	# 	return "<User %s>" % self.firstname

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



# Another table containing questions of users

class Question(db.Model):
	__tablename__ = "questions"
	id = db.Column(db.Integer, primary_key = True)
	questions = db.Column(db.String(500))
	topic = db.Column(db.String(500))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

# class Role():
# 	__tablename__ = 'roles'
# 	id = db.Column(db.Integer,primary_key = True)
# 	name = db.Column(db.String(64), unique = True)
# 	default = db.Column(db.Boolean, default = False, index = True)
# 	permissions = db.Column(db.Integer)
# 	users = db.relationship('User', backref = 'role', lazy = 'dynamic')

# 	def can(self,permissions):
# 		return self.role is not None and (self.role.permissions & permissions) == permissions

# 	def is_administrator(self):
# 		return self.can(Permission.ADMINISTER)

# 	@staticmethod
# 	def insert_roles():
# 		roles = {
# 			'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
# 			'Moderator': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS, False),
# 			'Administrator': (0xff, False)
# 		}
# 		for r in roles:
# 			role = Role.query.filter_by(name = r).first()
# 			if role is None:
# 				role = Role(name = r)
# 			role.permissions = roles[r][0]
# 			role.default = roles[r][1]
# 			db.session.add(role)
# 			db.session.commit()

# class Permission:
# 	FOLLOW = 0x01
# 	COMMENT = 0x02
# 	WRITE_ARTICLES = 0x04
# 	MODERATE_COMMENTS = 0x08
# 	ADMINISTER = 0x80

# class AnonymousUser(AnonymousUserMixin):
# 	def can(self,permissions):
# 		return False

# 	def is_administrator(self):
# 		return False
# login_manager.anonymous_user = AnonymousUser

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