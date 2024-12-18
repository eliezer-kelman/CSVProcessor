import os
from ensurepip import bootstrap

from dotenv import load_dotenv

load_dotenv()

# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# global_terrorism_1000 = os.path.join(base_dir, 'data', 'globalterrorismdb_0718dist-1000 rows.csv')

bootstrap_server = os.environ['BOOTSTRAP_SERVERS']

topic_mongo_writer = os.environ['MONGO_WRITER_TOPIC']