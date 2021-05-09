from os import environ 
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['TRELLO_API_KEY'] = environ.get('TRELLO_API_KEY')
app.config['TRELLO_SECRET_KEY'] = environ.get('TRELLO_SECRET_KEY')


from app.routes import *

# Register blueprint(s) 
app.register_blueprint(cards)