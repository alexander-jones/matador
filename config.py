import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False # https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
SQLALCHEMY_DATABASE_PATH = os.path.join(basedir, 'matador.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + SQLALCHEMY_DATABASE_PATH
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_migrations') 
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'