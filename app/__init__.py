import os
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

app = Flask(__name__)
from app.auth.views import admin
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SECRET_KEY'] = 'hard to guess string'
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.register_blueprint(auth.views.admin,url_prefix = '/authentication')
#app = create_app('DEVELOPMENT')

manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')