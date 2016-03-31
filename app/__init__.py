from flask import Flask
from flask.ext.bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_myapp():
	app = Flask(__name__)
	bootstrap.init_app(app)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app