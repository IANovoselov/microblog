import os

from dotenv import load_dotenv

# Установка переменных окружения из файла .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """
    Объект конфигурации
    """

    # Секретный ключ
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Настройки БД
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Пагинация
    POSTS_PER_PAGE = 3

    # Настройки почтового сервера
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 465))
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [os.environ.get('ADMINS')]

    # Поддерживаемые языки для перевода постов
    LANGUAGES = ['ru', 'en']

    # Настройки для доступа к API Яндекс переводчика
    TRANSLATE_TOKEN = os.environ.get('TRANSLATE_TOKEN')
    FOLDER_ID = os.environ.get('FOLDER_ID')

    # Полнотекстовый поиск Elasticsearch
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    # Словарь конфигурации для подключения к БД
    dbconfig = {'host': 'localhost',
                'port': '5432',
                'user': os.environ.get('DB_USER'),
                'password': os.environ.get('DB_PASS_WORD'),
                'dbname': 'microblog', }

    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
