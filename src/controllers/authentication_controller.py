import logging
from src import app
from src.utils.authentication import Authentication
from src.utils.logs_messages import LogsMessages
from src.utils.response_format import ResponseFormat

logs_messages = LogsMessages()
authentication = Authentication()
responses = ResponseFormat()
logger = logging.getLogger('Authentication Controller')


@app.route('/api/exchange-rate/token', methods=['GET'])
def get_auth_token():
    try:
        logger.info('Retrieving exchange rates')
        token = authentication.generate_auth_token()

        return responses.ok_response({'token': token.decode('ascii')})

    except Exception as error:
        logger.error(logs_messages.log_error(str(error)))

        return responses.error_response(str(error))


