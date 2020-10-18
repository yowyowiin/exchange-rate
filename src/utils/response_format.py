from flask import make_response


class ResponseFormat:
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