import redis
import time
from flask import Flask

app = Flask(__name__)

cache = redis.Redis(host="redis", port=6379)

def get_hit_count():
    retry=5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retry==0:
                raise exc
            retry -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    return "<h1>Hello Flask App! -> {}<h1>".format(count)