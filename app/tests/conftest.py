import pytest
from app.processors.data_csv_cleaner import clean_data
from app.readers.csv_reader import read_csv


@pytest.fixture(scope="module")
def cleaned_data():
    try:
        data = read_csv('../../data/globalterrorismdb_0718dist-1000 rows.csv')
    except Exception as e:
        pytest.fail(f"Failed to read CSV file: {e}")
    try:
        top_5 = data.head(5)
        cleaned_data = clean_data(top_5, relevant_columns, required_columns, fill_value=None)
    except KeyError as e:
        pytest.fail(f"Relevant columns missing: {e}")

    yield cleaned_data
