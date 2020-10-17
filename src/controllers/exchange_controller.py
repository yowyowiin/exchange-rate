import json

from bottle import HTTPResponse
from src.services.fixer import Fixer
from src import app

fixer = Fixer()


def ok_response(data=None) -> dict:
    response = {
        'status': 'OK'
    }
    if data or type(data) == list:
        response['rates'] = data

    return response


def error_response(data=None, status_code=500) -> HTTPResponse:
    if data is None:
        data = {}

    return HTTPResponse(
        body=json.dumps({'status': 'ERROR', 'error_message': data}),
        headers={'Content-Type': 'application/json'},
        status=status_code)


@app.route('/api/exchange-rate', method='GET')
def get_exchange_rate():
    rates = {
        'fixer': fixer.get_usd_to_mxn()
    }

    return ok_response(rates)
