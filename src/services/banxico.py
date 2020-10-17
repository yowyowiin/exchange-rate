import requests
from settings import BANXICO_TOKEN
from datetime import datetime
import pytz


class Banxico:

    @staticmethod
    def get_exchange_rate() -> requests.request:
        tz = pytz.timezone('America/Mexico_City')
        date = datetime.now(tz=tz).strftime('%Y-%m-%d')
        url = f'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/{date}/{date}?token={BANXICO_TOKEN}'

        response = requests.request('GET', url)

        return response

    def get_usd_to_mxn(self) -> dict:
        exchange = self.get_exchange_rate()
        response = {'last_updated': None, 'value': None}

        if exchange.status_code != 200:
            return response

        else:
            formated_exchange = exchange.json()['bmx']['series'][0]['datos'][0]
            timestamp = formated_exchange['fecha']
            value = formated_exchange['dato']

            response['last_updated'] = datetime.strptime(timestamp, '%d/%m/%Y').isoformat()
            response['value'] = float(value)

        return response

