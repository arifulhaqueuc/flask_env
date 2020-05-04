# projectX/config.py

import os
from os.path import join, dirname
from dotenv import load_dotenv

# OPTION 1>> how to detect the .env file path
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OPTION 2>> how to detect .env file path
# from pathlib import Path  # python3 only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)
# This idea failed.



SECRET_KEY_2000 = os.getenv('SECRET_KEY_2000')
print(SECRET_KEY_2000)

# Havenot tested it yet, how to use os.environ module
# SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")


# Test step 1
# Lets print something from this file to see 
# if we can read values from this file
GITHUB_TOEKN = 'hjkh'
print("This value is coming from this file")
print('GITHUB_TOEKN >>> ' + GITHUB_TOEKN)
# Status OK

# Test step 2
# Test if we can read values from .env file
BITBUCKET_TOEKN = os.getenv('BITBUCKET_TOEKN')
print("This value is coming from .env file")
print('BITBUCKET_TOEKN >>>' + BITBUCKET_TOEKN)
# Status OK


# Test step 3
# Test if we can read values from .env file
SECRET_KEY_2000 = os.getenv('SECRET_KEY_2000')
print("This value is coming from .env file")
print('SECRET_KEY_2000 >>>' + SECRET_KEY_2000)
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

