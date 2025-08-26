from decouple import config

class Config():
    SECRET_KEY = config('KEY')
    JWT_SECRET_KEY = config('JWT')

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5001

config = {
    'development': DevelopmentConfig
}