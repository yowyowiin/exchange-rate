import logging
from src import app
from src.controllers.exchange_controller import ok_response, error_response
from src.utils.authentication import Authentication
from src.utils.logs_messages import LogsMessages

logs_messages = LogsMessages()
authentication = Authentication()
logger = logging.getLogger('Authentication Controller')


@app.route('/api/exchange-rate/token', methods=['GET'])
def get_auth_token():
    try:
        logger.info('Retrieving exchange rates')
        token = authentication.generate_auth_token()

        return ok_response({'token': token.decode('ascii')})

    except Exception as error:
        logger.error(logs_messages.log_error(str(error)))

        return error_response(str(error))


