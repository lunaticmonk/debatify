import os
from flask import Blueprint
from flask import Flask,render_template,url_for,request,session,redirect
from flask_bootstrap import Bootstrap
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy
#from app import create_app
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

#app = create_app('DEVELOPMENT')

manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

auth = Blueprint('auth',__name__)
from  .import views

@app.route('/')
def index():
	return render_template('index.html')

# class User(db.Model):
# 	__tablename__ = 'users'
# 	id = db.Column(db.Integer,primary_key = True)
# 	username = db.Column(db.String(64),nullable = False)
# 	password = db.Column(db.String(100),nullable = False)
# 	password_hash = db.Column(db.String(128))
# 	firstname = db.Column(db.String(50),nullable = False)
# 	lastname = db.Column(db.String(50),nullable = False)

# 	def __repr__(self):
# 		return "<User %s>" % self.firstname



if __name__ == '__main__':
	manager.run()