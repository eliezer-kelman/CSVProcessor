from app.processors.validate import validate_dataframe
from app.tests.conftest import relevant_columns


def test_clean_data(cleaned_data):
    assert cleaned_data is not None
    assert len(cleaned_data) == 5
    assert 'eventid' in cleaned_data.columns
    assert 'iyear' in cleaned_data.columns
    assert set(cleaned_data.columns) == set(relevant_columns)
    assert 'irrelevant_column' not in cleaned_data
    print(cleaned_data)

def test_model_terror_event(cleaned_data):
    validated_data, errors = validate_dataframe(cleaned_data)
    print(f"Validated rows: {len(validated_data)}")
    print(f"Errors: {len(errors)}")


