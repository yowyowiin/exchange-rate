import requests
from datetime import datetime
from bs4 import BeautifulSoup


class DiarioOficial:

    @staticmethod
    def get_exchange_rate() -> requests.request:
        url = 'https://www.banxico.org.mx/tipcamb/tipCamMIAction.do'

        response = requests.request("GET", url)

        return response

    def get_usd_to_mxn(self) -> dict:
        exchange = self.get_exchange_rate()
        response = {'last_updated': None, 'value': None}

        if exchange.status_code != 200:
            return response

        else:
            exchange_html = exchange.text

            response['last_updated'] = self.__find_last_date(exchange_html)
            response['value'] = self.__find_mxn_exchange(exchange_html)

        return response

    @staticmethod
    def __find_mxn_exchange(html: str) -> float:
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('tr', class_='renglonNon')
        currency_row = data[0].find_all('td')[1]
        currency = str(currency_row).replace('<td align=\"right\">', '').replace('</td>', '').strip()

        return float(currency)

    @staticmethod
    def __find_last_date(html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('tr', class_='renglonNon')
        date_row = data[0].find_all('td')[0]
        date = str(date_row).replace('<td align=\"left\" style=\"padding-top:5px;padding-bottom:5px;\">', '')\
            .replace('</td>', '').strip()

        return datetime.strptime(date, '%d/%m/%Y').isoformat()
