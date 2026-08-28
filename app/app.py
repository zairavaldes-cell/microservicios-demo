import os
from flask import Flask
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'localhost')
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
        hostname = os.uname()[1]
        return f'¡Hola! Esta página ha sido visitada {count} veces. Atendido por el contenedor: {hostname}\n'
    except Exception as e:
        return f'Error al conectar con Redis: {str(e)}', 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
