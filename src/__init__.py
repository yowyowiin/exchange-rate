from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'You see, but you do not observe.'

from src.controllers import *
