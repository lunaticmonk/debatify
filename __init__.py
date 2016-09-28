import os
from flask import Flask,render_template,url_for
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from models import User
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

@app.route('/')
def index():
	return render_template('index.html')
	#return '<p>hello sumedh!</p>'			



if __name__ == '__main__':
	manager.run()