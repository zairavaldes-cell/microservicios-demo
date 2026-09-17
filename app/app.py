import os
import socket
from flask import Flask, render_template, jsonify
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'localhost')
# Añadimos decode_responses=True para que Redis devuelva strings y no bytes
cache = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# Ruta principal: Sirve la interfaz HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta API: Devuelve los datos en formato JSON para el JavaScript
@app.route('/api/data')
def get_data():
    try:
        count = cache.incr('hits')
        hostname = socket.gethostname()
        return jsonify({
            'count': count,
            'hostname': hostname,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # Forzar nuevo deploy - v2