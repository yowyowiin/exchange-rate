import requests
from settings import FIXER_API_KEY
from datetime import datetime


class Fixer:

    @staticmethod
    def get_exchange_rate() -> requests.request:
        url = f'http://data.fixer.io/api/latest?access_key={FIXER_API_KEY}'

        payload = {}
        headers = {
            'Cookie': '__cfduid=de4dc1d30ba1b2d1913f26d08165f4c641602897611'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    def get_usd_to_mxn(self) -> dict:
        exchange = self.get_exchange_rate()
        response = {'last_updated': None, 'value': None}

        if exchange.status_code != 200:
            return response

        else:
            formated_exchange = exchange.json()
            timestamp = formated_exchange['timestamp']
            value = self.__convert_usd_to_mxn(
                usd=formated_exchange['rates']['USD'],
                mxn=formated_exchange['rates']['MXN']
            )

            response['last_updated'] = datetime.fromtimestamp(timestamp).isoformat()
            response['value'] = value

        return response

    @staticmethod
    def __convert_usd_to_mxn(usd: float, mxn: float) -> float:
        return round(mxn/usd, 4)
