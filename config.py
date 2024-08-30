import os, sys

CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '1234'
    DEBUG = True
    CACHE_TYPE = 'simple'
    LOGIN_VIEW = 'login'

    BASE_DIR = CONFIG_DIR
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    IMGS_DIR = os.path.join(BASE_DIR, 'static', 'imgs')
    DATABASE_URI = os.path.join(BASE_DIR,'db','my_database.db')
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'contact@colinaanalytics.com'
    MAIL_PASSWORD = 'yblw skwu czgy ztcw'
    MAIL_TIMEOUT = 15