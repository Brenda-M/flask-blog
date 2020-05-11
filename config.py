import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  API_URL=os.environ.get('API_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  MAIL_SERVER = 'smtp.googlemail.com' 
  MAIL_PORT = 587
  MAIL_USE_TLS = True 
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Bm19952810@localhost/personalblog_test'


class DevConfig (Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Bm19952810@localhost/personalblog'
  DEBUG = True

class ProdConfig (Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test': TestConfig
}
