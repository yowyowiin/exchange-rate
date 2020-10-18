from settings import DUMMY_USER_ID, EXPIRATION_TIME
from src import app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired


class Authentication:
    id = DUMMY_USER_ID

    def generate_auth_token(self, expiration=EXPIRATION_TIME) -> bytes:
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)

        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token: str) -> bool:
        s = Serializer(app.config['SECRET_KEY'])
        try:
            s.loads(token)
        except SignatureExpired:
            raise SignatureExpired('Token has expired')  # valid token, but expired
        except BadSignature:
            raise BadSignature('Invalid token')  # invalid token

        return True
