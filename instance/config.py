import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'afdfsdf')

DB_USERNAME = os.environ.get('DB_USERNAME', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 1)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'sample')
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True
