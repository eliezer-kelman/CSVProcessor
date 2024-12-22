import pandas as pd
import app.readers.csv_reader as csv_reader
from app.utils.params_dtype import dtype


def load_and_merge_files(file_1_path, file_2_path):
    df_1 = csv_reader.read_csv(file_1_path)
    df_2 = csv_reader.read_csv(file_2_path, dtype=dtype) # קובץ גדול
    df_1['Date'] = pd.to_datetime(df_1['Date'], format='%d-%b-%y', errors='coerce')

    df_2['iyear'] = df_2['iyear'].fillna(1).astype(int)
    df_2['imonth'] = df_2['imonth'].fillna(1).astype(int)
    df_2['iday'] = df_2['iday'].fillna(1).astype(int)

    df_2['date'] = pd.to_datetime(
        df_2['iyear'].astype(str) + '-' + df_2['imonth'].astype(str) + '-' + df_2['iday'].astype(str), errors='coerce')

    df_2['date'] = df_2['date'].fillna(pd.Timestamp('1800-01-01'))

    if df_2['date'].isnull().any():
        print("Warning: Some dates in df_2 could not be parsed and are set to NaT.")

    df_1 = df_1.sort_values(by=['Date', 'City', 'Country'])

    merged_df = pd.merge(
        df_2,
        df_1[['Date', 'City', 'Country', 'Description']],
        how='left',
        left_on=['date', 'city', 'country_txt'],
        right_on=['Date', 'City', 'Country']
    )

    merged_df['date'] = merged_df['date'].apply(lambda x: x.isoformat() if pd.notnull(x) else None)

    return merged_df
