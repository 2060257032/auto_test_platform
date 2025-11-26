from flask import Flask
import redis # type: ignore

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis_client.incr('visitor_count')
    return f'Hello! Visitor count: {count}'

@app.route('/api/visitors')
def visitors():
    count = redis_client.get('visitor_count') or 0
    return {'visitor_count': int(count)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)