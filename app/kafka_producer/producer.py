from kafka import KafkaProducer
import json
from app.settings.config import bootstrap_server

def send_to_kafka(data, topic):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_server,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    for record in data:
        producer.send(topic, value=record)
    producer.flush()
