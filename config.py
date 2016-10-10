import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql6138801:Nefp9ZvUCA@sql6.freemysqlhosting.net/sql6138801'

class Development(Config):
	DEBUG = True

class Production(Config):
	DEBUG = True

class Testing(Config):
	DEBUD = True

config = {
	'CONFIG' : Config,
	'DEVELOPMENT' : Development,
	'PRODUCTION' : Production,
	'TESTING' : Testing
}
