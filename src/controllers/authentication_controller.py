import logging
from flask import make_response
from src import app
from src.utils.authentication import Authentication
from src.utils.logs_messages import LogsMessages

logs_messages = LogsMessages()
authentication = Authentication()
logger = logging.getLogger('Authentication Controller')


def ok_response(data=None) -> dict:
    response = {
        'status': 'OK'
    }
    if data or type(data) == list:
        response['rates'] = data

    return response


def error_response(data=None, status_code=500) -> make_response:
    if data is None:
        data = {}

    resp = make_response({'status': 'ERROR', 'error_message': data}, status_code)

    return resp


@app.route('/api/exchange-rate/token', methods=['GET'])
def get_auth_token():
    try:
        logger.info('Retrieving exchange rates')
        token = authentication.generate_auth_token()

        return ok_response({'token': token.decode('ascii')})

    except Exception as error:
        logger.error(logs_messages.log_error(str(error)))

        return error_response(str(error))


