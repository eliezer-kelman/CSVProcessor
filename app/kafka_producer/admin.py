import os
from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

from app.settings.config import bootstrap_server, topic_mongo_writer, num_partitions, num_replication

load_dotenv(verbose=True)

def init_topics():
    client = KafkaAdminClient(bootstrap_servers=bootstrap_server)
    new_member_topic = NewTopic(
        name=topic_mongo_writer,
        num_partitions=int(num_partitions),
        replication_factor=int(num_replication)
    )
    try:
        client.create_topics([new_member_topic])
    except TopicAlreadyExistsError as e:
        print(e)
    finally:
        client.close()