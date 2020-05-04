# settings.py

# OR, the same with increased verbosity
# load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
# from pathlib import Path  # python3 only
# env_path = Path('.') / '.flaskenv'
# load_dotenv(dotenv_path=env_path)


# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

# OPTION 1>> how to detect the .env file path
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OPTION 2>> how to detect .env file path
# from pathlib import Path  # python3 only
# env_path = Path('.') / '.flaskenv'
# load_dotenv(dotenv_path=env_path)



SECRET_KEY_889 = 'QQuuGGH'
SECRET_KEY_1000 = 'QQuuGGHVVVVVV'
SECRET_KEY_2000 = os.getenv('SECRET_KEY_2000')
print(SECRET_KEY_2000)

DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
# Havenot tested it yet, how to use os.environ module
# SECRET_KEY = os.environ.get("SECRET_KEY")


# Test step 1
# Lets print something from this file to see 
# if we can read values from this file
GITHUB_TOEKN = 'hjkh'
print('printing GITHUB_TOEKN for test ' + GITHUB_TOEKN)
# Status OK

# Test step 2
# Test if we can read values from .env file
BITBUCKET_TOEKN = os.getenv('BITBUCKET_TOEKN')
print('printing BITBUCKET_TOEKN for test ' + BITBUCKET_TOEKN)
# Status OK



class BaseConfig():
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(BaseConfig):
    DATABASE_URI = 'mysql://user@localhost/foo'
    GITLAB_TOEKN = os.getenv('BITBUCKET_TOEKN')
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True






