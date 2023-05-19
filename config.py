import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3

    MAIL_SERVER = 'smtp.rambler.ru'
    MAIL_PORT = int(465)
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'flasktest@rambler.ru'
    MAIL_PASSWORD = 'FlasK_test6'
    ADMINS = ['flasktest@rambler.ru']

    LANGUAGES = ['ru', 'en']

    TRANSLATE_TOKEN = "t1.9euelZqez5WMlp6ZyM2dz5uUlJaTj-3rnpWax4_HnM-TyMfKi5yLi4-OmZrl8_dlY2xc-e8sGXM-_N3z9yUSalz57ywZcz78.sI0wX2RTPXg5cHeAh14zonFQ-FXcOp-x93HSTodN2plz4eVzPFyIweCp3izbFHuGVk2GW57DR5ILx3oU8vSsBw"
    FOLDER_ID = "b1gftt55ulpmcjat4vvs"