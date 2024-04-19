import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration class. Contain default configuration settings."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')


class DevelopmentConfig(Config):
    """Development configuration class. Contain configuration settings for development."""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default="sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.db"))


class ProductionConfig(Config):
    """ Production configuration. """
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default='sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db'))


class TestingConfig(Config):
    """ Testing configuration. """
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'testing' 
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.db")


def get_config_by_name(config_name):
    """ Get configuration by name. """
    if config_name == 'development':
        return DevelopmentConfig()
    elif config_name == 'production':
        return ProductionConfig()
    elif config_name == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig()