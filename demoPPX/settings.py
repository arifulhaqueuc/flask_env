#demo/settings.py
import os 

SECRET_KEY = os.environ.get('SECRET_KEY')
API_KEY = os.environ.get('API_KEY')
GITLAB_TOEKN = os.environ.get('GITLAB_TOEKN')

