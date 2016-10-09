import os
from flask import Flask,render_template,url_for,request,session,redirect
from flask.ext.login import LoginManager
from flask_bootstrap import Bootstrap
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6138801:Nefp9ZvUCA@sql6.freemysqlhosting.net/sql6138801'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SECRET_KEY'] = 'hard to guess string'
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app = create_app('DEVELOPMENT')

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.process'

from app import models

@app.route('/')
def index():
    return render_template('index.html')

from app.auth.views import admin
app.register_blueprint(auth.views.admin,url_prefix = '/authentication')

from app.main.views import welcome
app.register_blueprint(main.views.welcome,url_prefix = '/welcome')
