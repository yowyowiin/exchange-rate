import logging
from flask import request, make_response

from settings import USER_RATE_LIMIT
from src.services.fixer import Fixer
from src.services.diario_oficial import DiarioOficial
from src.services.banxico import Banxico
from src import app
from src.utils.authentication import Authentication
from src.utils.cache_memory import CacheMemory
from src.utils.logs_messages import LogsMessages
from itsdangerous import (BadSignature, SignatureExpired)

from src.utils.response_format import ResponseFormat

logs_messages = LogsMessages()
fixer = Fixer()
diario_oficial = DiarioOficial()
banxico = Banxico()
authentication = Authentication()
cache_memory = CacheMemory()
responses = ResponseFormat()

logger = logging.getLogger('Exchange Controller')


@app.route('/api/exchange-rate', methods=['GET'])
def get_exchange_rate():
    try:
        logger.info('Retrieving exchange rates')
        if 'token' not in request.headers or 'user' not in request.headers:
            return responses.error_response('token or user headers are missing', status_code=400)

        token = request.headers['token']
        user = request.headers['user']

        if authentication.verify_auth_token(token):
            if cache_memory.check_element_existence(user) and \
                    int(cache_memory.get_element(user).decode('utf-8')) >= USER_RATE_LIMIT:
                return responses.error_response('User requests exceeded', status_code=429)
            else:
                cache_memory.save_user_request(user, 1)
                rates = {
                    'diario_oficial_de_la_federacion': diario_oficial.get_usd_to_mxn(),
                    'fixer': fixer.get_usd_to_mxn(),
                    'banxico': banxico.get_usd_to_mxn()
                }

                return responses.ok_response(rates)

    except (SignatureExpired, BadSignature) as error:
        logger.error(logs_messages.log_error(str(error)))

        return responses.error_response(str(error), status_code=401)

    except Exception as error:
        logger.error(logs_messages.log_error(str(error)))

        return responses.error_response(str(error))


