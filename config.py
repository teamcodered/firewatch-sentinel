import os
import json

from dotenv import load_dotenv

load_dotenv()

def load_remote_connection_info():
    if os.environ.get('VCAP_SERVICES') is not None:
        envstr = os.environ.get('VCAP_SERVICES')        
        vcap = json.loads(envstr)
        if 'dashDB for Transactions' in vcap:
            db_uri = vcap['dashDB for Transactions']['credentials']['uri']
            return db_uri
    else:
        return None
    

class Config:

    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = 'secret456'

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./firewatch.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'firewatch.db')
    FLASK_ADMIN_SWATCH = 'cerulean'
    
    CELERY_BROKER_URL = 'amqp://nnghcsne:D_bwsuaOhb4nu76ZcX_5Qlc0z0peVNKx@orangutan.rmq.cloudamqp.com/nnghcsne'
    CELERY_RESULT_BACKEND = 'db+sqlite:///task-results.sqlite'
    # SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']

class DevConfig(Config):
    TESTING = True
    DEBUG = True

class ProdConfig(Config):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # CELERY_RESULT_BACKEND = 'rpc:///'
    # SQLALCHEMY_ENGINE_OPTIONS = {'connect_args': {'DB2_DEFERRED_PREPARE_SEMANTICS': 'yes'}}

class RemoteProdConfig(Config):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'db2://tcc29831:l0fx4bnrm6h8j0-g@dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net:50000/BLUDB'
    CELERY_RESULT_BACKEND = 'db+db2://tcc29831:l0fx4bnrm6h8j0-g@dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net:50000/BLUDB'

class SQLiteProdConfig(Config):
    TESTING = False
    DEBUG = False

class ProdPostgresConfig(Config):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:5Irryft2xoat4waG@35.202.56.48/firewatch'
    CELERY_RESULT_BACKEND = 'postgresql://postgres:5Irryft2xoat4waG@35.202.56.48/firewatch'