import socket

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, socket_connect_timeout=5)
host = socket.gethostname()


@app.route('/')
def hello():
    redis.incr('hits')
    return '''
               Hello world! I have been seen % times.
               My hostname is %
           ''' % (redis.get('hits'), host)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
