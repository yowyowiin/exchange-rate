from bottle import run
from src import app

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8085, server='tornado')
