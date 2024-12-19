from kafka import KafkaProducer
import json
from app.settings.config import bootstrap_server

def send_to_kafka(data, topic):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_server,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    producer.send(topic, value=data)
    producer.flush()
