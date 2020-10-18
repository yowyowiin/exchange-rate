import logging

from settings import APP_PORT
from src import app

logging.basicConfig(
    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger('Server')

if __name__ == '__main__':
    logger.info('Starting App')
    app.run(port=APP_PORT, host='0.0.0.0')
