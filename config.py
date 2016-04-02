import os

basedir = os.path.abspath(os.path.dirname(__file__))


class config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
	DEBUG = True
	OAUTH_CREDENTIALS = {
		'facebook':{
			'id': os.environ.get('FACEBOOK_ID_LOCAL'),
			'secret': os.environ.get('FACEBOOK_SECRET_LOCAL')
		}
	}
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	@staticmethod
	def init_app(app):
		pass

