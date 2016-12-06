import os
from flask import Flask,render_template,url_for,request,session,redirect
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_socketio import SocketIO
from flask_gravatar import Gravatar

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6140009:Y1912zwYwC@sql6.freemysqlhosting.net/sql6140009'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess string'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

manager = Manager(app)
bootstrap = Bootstrap()
db = SQLAlchemy(app)
mail = Mail(app)
moment = Moment(app)
socketio = SocketIO(app)
gravatar = Gravatar(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
# app.config['SECRET_KEY'] = 'hard to guess string'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#app = create_app('DEVELOPMENT')

bootstrap.init_app(app)
#db.init_app(app)
login_manager.init_app(app)

from app import models

@app.route('/')
def index():
    return render_template('index.html')

from app.auth.views import admin
app.register_blueprint(auth.views.admin,url_prefix = '/authentication')

from app.main.views import welcome
app.register_blueprint(main.views.welcome,url_prefix = '/welcome')

from app.twitterAPI.views import api
app.register_blueprint(twitterAPI.views.api,url_prefix = '/api')
