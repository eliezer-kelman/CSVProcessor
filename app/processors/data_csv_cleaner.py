
# Selects only relevant columns from the DataFrame.
def filter_relevant_columns(data, columns):
    try:
        filtered_data = data[columns]
        return filtered_data
    except KeyError as e:
        print(f"Error: One or more columns are missing: {e}")
        return None

# Fills in missing values
def fill_missing_values(data, fill_value=None):
    if fill_value is None:
        return data
    else:
        return data.fillna(fill_value)


# Removes rows that have missing values in critical columns.
def drop_invalid_rows(data, required_columns):
    return data.dropna(subset=required_columns)


def clean_data(data, relevant_columns, required_columns, fill_value=None):
    data = filter_relevant_columns(data, relevant_columns)
    if data is None:
        return None
    data = fill_missing_values(data, fill_value)
    data = drop_invalid_rows(data, required_columns)
    return data
