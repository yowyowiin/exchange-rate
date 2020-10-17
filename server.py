from bottle import run
from src import app
from settings import APP_HOST

if __name__ == '__main__':
    run(app, host=APP_HOST, port=8085, server='tornado')
