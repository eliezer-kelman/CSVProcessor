from app.models.terror_event import TerrorEvent
from app.utils.convert_utils import convert_row_to_terror_event


def validate_dataframe(dataframe):
    validated_data = []
    errors = []
    for _, row in dataframe.iterrows():
        try:
            dic = convert_row_to_terror_event(row)
            event = TerrorEvent(**dic)
            validated_data.append(event)
        except Exception as e:
            errors.append((row.to_dict(), str(e)))
    return validated_data, errors

