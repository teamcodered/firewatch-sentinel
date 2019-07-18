import os

class Config:

    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./firewatch.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'firewatch.db')
    # SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']

class DevConfig(Config):
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
