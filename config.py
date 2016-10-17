import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'

	@staticmethod
    def init_app(app):
        pass

class Development(Config):
	DEBUG = True

class Production(Config):
	DEBUG = True

class Testing(Config):
	DEBUG = True

config = {
	'CONFIG' : Config,
	'DEVELOPMENT' : Development,
	'PRODUCTION' : Production,
	'TESTING' : Testing
}
