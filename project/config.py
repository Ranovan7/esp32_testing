import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = os.environ.get('DATABASE_URI', 'postgresql://postgres:@localhost/')
database_name = os.environ.get('DATABASE_NAME', 'flask_jwt_auth')


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious')
    OCR_SPACE_API_KEY = os.environ.get('OCR_SPACE_API_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SECRET_KEY = 'my_precious'
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'my_precious'
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + "_test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name
