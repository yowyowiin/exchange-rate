import logging
from settings import APP_HOST
from bottle import run
from src import app

logging.basicConfig(
    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger('Server')

if __name__ == '__main__':
    logger.info('Starting App')
    run(app, host=APP_HOST, port=8085, server='tornado')
