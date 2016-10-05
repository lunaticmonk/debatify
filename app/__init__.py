import os
from flask import Flask,render_template,url_for,request,session,redirect
from flask_bootstrap import Bootstrap
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy
#from app import *
#from app import create_app
#from models import User
#from flask.ext.sqlalchemy import SQLAlchemy
#from models import User
#from flask_wtf import Form
#from wtforms.validators import Required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6138801:Nefp9ZvUCA@sql6.freemysqlhosting.net/sql6138801'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
from app import models
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SECRET_KEY'] = 'hard to guess string'
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app = create_app('DEVELOPMENT')


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

@app.route('/')
def index():
    return render_template('index.html')

from app.auth.views import admin
app.register_blueprint(auth.views.admin,url_prefix = '/authentication')
