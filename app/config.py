import os


class Config:
    SECRET_KEY = '87f311180775b5278c2eb23c26a6a555'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'gharidev1511'
    MAIL_PASSWORD = 'mybook1511'