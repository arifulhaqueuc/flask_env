from flask import Flask
# from flask import current_app


app = Flask(__name__)
app.config.from_pyfile('config.py')

# app.config.from_envvar('YOURAPPLICATION_SETTINGS')
# app.config.from_object(".config.ProductionConfig")
# app.config.from_object('settings.ProductionConfig')
# hoon = app.config['SECRET_KEY_1000']

# app.config['SECRET_KEY_1000']
# This is wrong


# how get a value from config.py file
# app.config.get("SECRET_KEY_2000")


@app.route('/ppo')
def some667():
	res = 'ARIFULHAQUE2020'
	if (res == app.config.get("SECRET_KEY_2000")):
		return 'i have the sec key value'
	else:
		return 'today is sunday'



@app.route('/')
def sunday999():
	return app.config.get("SECRET_KEY_2000")
	

