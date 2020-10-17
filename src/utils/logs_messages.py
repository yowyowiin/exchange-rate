class LogsMessages:
    @staticmethod
    def log_error(message: str) -> dict:
        return {'code': 'Error', 'message': message}
