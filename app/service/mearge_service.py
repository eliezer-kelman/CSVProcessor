import pandas as pd
import app.readers.csv_reader as csv_reader
from app.utils.params_dtype import dtype


def load_and_merge_files(file_1_path, file_2_path):
    # טוען את הקובץ הקטן (RAND) ואת הקובץ הגדול (globalterrorism) עם קידוד ספציפי
    df_1 = csv_reader.read_csv(file_1_path)
    print(df_1.head(2))
    df_2 = csv_reader.read_csv(file_2_path, dtype=dtype) # הקובץ הגדול (globalterrorism)
    print(df_2.head(2))
    # נרמל את פורמט התאריך בקובץ הראשון (RAND)
    df_1['Date'] = pd.to_datetime(df_1['Date'], format='%d-%b-%y', errors='coerce')

    # טיפול בערכים חסרים בקובץ השני (df_2) לפני המרת התאריך
    df_2['iyear'] = df_2['iyear'].fillna(1).astype(int)  # אם חסרה שנה, נמלא ב-1
    df_2['imonth'] = df_2['imonth'].fillna(1).astype(int)  # אם חסר חודש, נמלא ב-1
    df_2['iday'] = df_2['iday'].fillna(1).astype(int)  # אם חסר יום, נמלא ב-1

    # המרת כל עמודת התאריך בנפרד
    df_2['date'] = pd.to_datetime(
        df_2['iyear'].astype(str) + '-' + df_2['imonth'].astype(str) + '-' + df_2['iday'].astype(str), errors='coerce')

    df_2['date'] = df_2['date'].fillna(pd.Timestamp('1800-01-01'))

    # בדוק אם התאריכים הומרו בהצלחה
    if df_2['date'].isnull().any():
        print("Warning: Some dates in df_2 could not be parsed and are set to NaT.")

    # ממיין את הקובץ הראשון (RAND) לפי תאריך, עיר ומדינה כדי לוודא שהאירוע הראשון ביום יתמזג
    df_1 = df_1.sort_values(by=['Date', 'City', 'Country'])

    # מבצע את המיזוג בין שני הקבצים על פי תאריך, עיר ומדינה, ושומר את כל העמודות מהקובץ הגדול
    merged_df = pd.merge(
        df_2,  # שומר את כל העמודות מהקובץ הגדול
        df_1[['Date', 'City', 'Country', 'Description']],  # לוקח רק את העמודה Description מהקובץ הקטן
        how='left',  # מיזוג בסוג 'left' כך שכל הנתונים בקובץ הגדול יישמרו
        left_on=['date', 'city', 'country_txt'],  # מיזוג על פי תאריך, עיר ומדינה בקובץ הגדול
        right_on=['Date', 'City', 'Country']  # מיזוג על פי תאריך, עיר ומדינה בקובץ הקטן
    )

    merged_df['date'] = merged_df['date'].apply(lambda x: x.isoformat() if pd.notnull(x) else None)

    return merged_df