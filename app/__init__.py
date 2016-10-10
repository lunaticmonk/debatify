import os
from flask import Flask,render_template
from flask.ext.login import LoginManager
from flask_bootstrap import Bootstrap
from flask_script import Manager,Shell
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.process'
manager = Manager()
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)

	from app.auth.views import admin
	app.register_blueprint(auth.views.admin,url_prefix = '/authentication')

	from app.main.views import welcome
	app.register_blueprint(main.views.welcome,url_prefix = '/welcome')


	@app.route('/')
	def index():
		return render_template('index.html')

	return app

