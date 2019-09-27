import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-n0mber-beTween-tHe-fir$t-ch1nese-letter-and-the-last-roman-numeral'
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
        # "postgresql://user:password@localhost/spaceshipDB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False