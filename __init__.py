import os
from flask import Flask,render_template,url_for,request,session,redirect
from flask_bootstrap import Bootstrap
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy
#from models import User
#from flask.ext.sqlalchemy import SQLAlchemy
#from models import User
#from flask_wtf import Form
#from wtforms.validators import Required

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

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


@app.route('/', methods = ['GET','POST'])
def index():
	if form.validate_on_submit():
		first_name = request.form['first_name']
		if first_name == User.query.filter_by(first_name).first():
			session['known'] = False
			return render_template('me.html', name = firstname, known = True )
		else:
			session['known'] = True
			firstname = User(firstname = first_name)
			db.session.add(firstname)
			return render_template('me.html', known = session.get('known',False))
	return render_template('index.html')
	#return '<p>hello sumedh!</p>'			

if __name__ == '__main__':
	manager.run()