import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	pass

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