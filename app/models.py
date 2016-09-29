from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(64),nullable = False)
	password = db.Column(db.String(100),nullable = False)
	password_hash = db.Column(db.String(128))
	firstname = db.Column(db.String(50),nullable = False)
	lastname = db.Column(db.String(50),nullable = False)

	def __repr__(self):
		return "<User %s>" % self.firstname