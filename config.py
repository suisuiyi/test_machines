import os
import pymysql

SECRET_KEY = os.urandom(24)

HOST = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'dada1234'
DATABASE = 'test_machine'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@localhost:3306/test_machine"
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True