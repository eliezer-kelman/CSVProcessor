from app.kafka_producer.admin import init_topics
from app.kafka_producer.producer import send_to_kafka
from app.processors.data_csv_cleaner import clean_data
from app.service.mearge_service import load_and_merge_files
from app.settings.config import topic_mongo_writer
from app.utils.data_utils import relevant_columns, required_columns
from app.utils.convert_utils import convert_row_to_terror_event
from app.utils.params_dtype import dtype

file_1_path = '../data/RAND_Database_of_Worldwide_Terrorism_Incidents - 5000 rows.csv'

file_2_path = '../data/globalterrorismdb_0718dist-1000 rows.csv'

if __name__ == "__main__":
    init_topics()
    data = load_and_merge_files(file_1_path, file_2_path)
    cleaned_data = clean_data(data, relevant_columns, required_columns, fill_value=None)
    for _, row in data.iterrows():
        try:
            event = convert_row_to_terror_event(row)
            print(event)
            send_to_kafka(event, topic_mongo_writer)
        except Exception as e:
            print(e)
            continue
