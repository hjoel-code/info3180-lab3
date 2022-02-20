import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'KNIO922oenn*@no2NOEU@@!*@!UOHHKWL')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.mailtrap.io')
    MAIL_PORT = os.environ.get('MAIL_PORT', '587')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '52dd23da0eb8de')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'b7225e1e05357b')
