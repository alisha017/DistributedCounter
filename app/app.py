from flask import Flask, request, jsonify
from counter import DistributedCounter
import os

app = Flask(__name__)
kafka_servers = [os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')]
topic = 'distributed_counter'
counter = DistributedCounter(kafka_servers, topic)


@app.route('/increment', methods=['POST'])
def increment():
    counter.increment()
    return jsonify({'message': 'Increment request received'}), 200


@app.route('/value', methods=['GET'])
def get_value():
    return jsonify({'value': counter.get_value()}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
