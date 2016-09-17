import os

basedir = os.path.abspath(os.path.dirname(__file__))


class config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
	DEBUG = True
<<<<<<< HEAD
	OAUTH_CRENDENTIALS = {
=======
	OAUTH_CREDENTIALS = {
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e
		'facebook':{
			'id': os.environ.get('FACEBOOK_ID_LOCAL'),
			'secret': os.environ.get('FACEBOOK_SECRET_LOCAL')
		},
		'qq':{
			'id': os.environ.get('QQ_ID_LOCAL'),
			'secret': os.environ.get('QQ_SECRET_LOCAL')
		}
	}
<<<<<<< HEAD

=======
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
>>>>>>> f2d69d82237baac92bfde3a4dc5193c3721c3c2e
	@staticmethod
	def init_app(app):
		pass

