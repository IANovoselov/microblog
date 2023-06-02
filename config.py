import os

from dotenv import load_dotenv

# Установка переменных окружения
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """
    Объект конфигурации
    """

    # Секретный ключ
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Настройки БД
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
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
