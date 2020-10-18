import redis
from datetime import timedelta

from settings import LIFETIME

r = redis.Redis()


class CacheMemory:
    @staticmethod
    def save_element(key: str, value: any, lifetime: int = LIFETIME):
        r.setex(
            key,
            timedelta(seconds=lifetime),
            value=value
        )

    @staticmethod
    def check_element_existence(key: str):
        return r.exists(key)

    @staticmethod
    def get_element(key: str):
        return r.get(key)

    @staticmethod
    def get_element_lifetime(key: str):
        return r.ttl(key)

    def save_user_request(self, key: str, value: any):
        if self.check_element_existence(key):
            requests = self.get_element(key).decode('utf-8')
            lifetime = self.get_element_lifetime(key)
            self.save_element(key, value + int(requests), lifetime=lifetime)

        else:
            self.save_element(key, value)
