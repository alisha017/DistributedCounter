import threading
from kafka import KafkaProducer, KafkaConsumer
import json
import os
import time


class DistributedCounter:
    def __init__(self, kafka_servers, topic):
        self.kafka_servers = kafka_servers
        self.topic = topic
        self.counter = 0
        self.lock = threading.Lock()
        self.producer = None
        self.consumer = None

        # Retry mechanism for Kafka producer and consumer
        for _ in range(5):
            try:
                self.producer = KafkaProducer(bootstrap_servers=kafka_servers,
                                              value_serializer=lambda v: json.dumps(v).encode('utf-8'))
                self.consumer = KafkaConsumer(topic,
                                              bootstrap_servers=kafka_servers,
                                              value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                              auto_offset_reset='earliest',
                                              enable_auto_commit=True)
                break
            except Exception as e:
                print(f"Error connecting to Kafka: {e}")
                time.sleep(5)
        else:
            raise Exception("Could not connect to Kafka after several attempts")

        self.consumer_thread = threading.Thread(target=self._consume_messages)
        self.consumer_thread.start()

    def increment(self):
        self.producer.send(self.topic, {'action': 'increment'})

    def get_value(self):
        with self.lock:
            return self.counter

    def _consume_messages(self):
        for message in self.consumer:
            with self.lock:
                if message.value['action'] == 'increment':
                    self.counter += 1
