import app.readers.csv_reader as csv_reader
from app.kafka_producer.producer import send_to_kafka
from app.settings.config import topic_mongo_writer
from app.utils.convert_utils import convert_row_to_terror_event
from app.utils.params_dtype import dtype

if __name__ == "__main__":
    data = csv_reader.read_csv('../data/globalterrorismdb_0718dist-1000 rows.csv', dtype=dtype)
    for _, row in data.iterrows():
        try:
            event = convert_row_to_terror_event(row)
            print(event)
            send_to_kafka(event, topic_mongo_writer)
        except Exception as e:
            print(e)
            continue
