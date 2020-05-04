# demo/__init__.py
from flask import Flask 

def create_app():
	app = Flask(__name__)
	# how to load the corresponding settings file
	app.config.from_pyfile('settings.py')


	@app.route('/')
	def index():
		return f'get api key value = { app.config.get("GITLAB_TOEKN") }'

	return app