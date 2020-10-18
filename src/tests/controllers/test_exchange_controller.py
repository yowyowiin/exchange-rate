from app import app
import unittest
import json
from mockito import when

from settings import USER_RATE_LIMIT
from src.controllers.exchange_controller import banxico, diario_oficial, fixer, cache_memory


class TestExchangeController(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_exchange_rate_then_ok(self):
        cache_memory.flush_cache()
        get_token = json.loads(self.app.get('/api/exchange-rate/token').data)
        token = get_token['rates']['token']
        mock_exchange = {
            'last_updated': '2020-10-18T00:00:00',
            'value': 21.3832
        }
        when(banxico).get_usd_to_mxn(...).thenReturn(mock_exchange)
        when(fixer).get_usd_to_mxn(...).thenReturn(mock_exchange)
        when(diario_oficial).get_usd_to_mxn(...).thenReturn(mock_exchange)

        response = self.app.get('/api/exchange-rate', headers={'user': 'test', 'token': token})
        data = json.loads(response.data)
        expected_response = {
            'rates': {
                'banxico': mock_exchange,
                'diario_oficial_de_la_federacion': mock_exchange,
                'fixer': mock_exchange
            },
            'status': 'OK'
        }

        assert 200 == response.status_code
        assert expected_response == data

    def test_get_exchange_rate_expired_token_then_unauthorized(self):
        cache_memory.flush_cache()
        token = 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMzA0OTI4MywiZXhwIjoxNjAzMDQ5ODgzfQ.eyJpZCI6MTIzfQ.WJ-UHOrOoGRlwW24A1' \
                'F1rw05L1HmX2i4r9YrgQUQDhBAcrjDEw08O2KaAcsFvwosqNQyFD5Lifn1WwlepeOu6Q'
        response = self.app.get('/api/exchange-rate', headers={'user': 'test', 'token': token})
        data = json.loads(response.data)

        assert 401 == response.status_code
        assert {'status': 'ERROR', 'error_message': 'Token has expired'} == data

    def test_get_exchange_rate_invalid_token_then_unauthorized(self):
        cache_memory.flush_cache()
        token = 'sajhc3uu0983ljkn'
        response = self.app.get('/api/exchange-rate', headers={'user': 'test', 'token': token})
        data = json.loads(response.data)

        assert 401 == response.status_code
        assert {'status': 'ERROR', 'error_message': 'Invalid token'} == data

    def test_get_exchange_no_headers_then_bad_request(self):
        cache_memory.flush_cache()
        response = self.app.get('/api/exchange-rate', headers={})
        data = json.loads(response.data)

        assert 400 == response.status_code
        assert {'status': 'ERROR', 'error_message': 'token or user headers are missing'} == data

    def test_get_exchange_rate_requests_exceeded_then_bad_request(self):
        cache_memory.flush_cache()
        get_token = json.loads(self.app.get('/api/exchange-rate/token').data)
        token = get_token['rates']['token']
        mock_exchange = {
            'last_updated': '2020-10-18T00:00:00',
            'value': 21.3832
        }
        when(banxico).get_usd_to_mxn(...).thenReturn(mock_exchange)
        when(fixer).get_usd_to_mxn(...).thenReturn(mock_exchange)
        when(diario_oficial).get_usd_to_mxn(...).thenReturn(mock_exchange)

        for i in range(USER_RATE_LIMIT + 1):
            response = self.app.get('/api/exchange-rate', headers={'user': 'test', 'token': token})
        data = json.loads(response.data)
        expected_response = {
            'error_message': 'User requests exceeded',
            'status': 'ERROR'
        }

        assert 429 == response.status_code
        assert expected_response == data
