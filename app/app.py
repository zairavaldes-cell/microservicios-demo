import os
import socket
from flask import Flask
import redis

app = Flask(__name__)

# Conexión a Redis usando el nombre del servicio definido en docker-compose
redis_host = os.getenv('REDIS_HOST', 'redis')
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

@app.route('/')
def hello():
    # Incrementa el contador en Redis
    visits = r.incr('counter')
    # Obtiene el ID del contenedor actual para demostrar balanceo de carga
    hostname = socket.gethostname()
    return f"<h1>¡Hola desde el microservicio!</h1><p>Esta página ha sido visitada <b>{visits}</b> veces.</p><p>Atendido por el contenedor: <code>{hostname}</code></p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)