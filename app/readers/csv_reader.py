import pandas as pd


def read_csv(file_path, delimiter=",", encoding='iso-8859-1', dtype=None):
    try:
        data = pd.read_csv(file_path, delimiter=delimiter, dtype=dtype , encoding=encoding)
        return data
    except Exception as e:
        print(f"Error reading CSV file at {file_path}: {e}")
        return None
