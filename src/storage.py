import redis
import os

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(REDIS_URL)


def set(key, value):
    r.set(key, value)


def get(key):
    return r.get(key)
