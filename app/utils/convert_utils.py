import pandas as pd
from app.models.terror_event import TerrorEvent


def convert_row_to_terror_event(row):
    try:
        row = row.where(pd.notnull(row), None)
        event = TerrorEvent(
            eventid=row['eventid'],
            date={"year": row['iyear'], "month": row['imonth'], "day": row['iday']},
            location={
                "country": row['country_txt'],
                "region": row['region_txt'],
                "province": row['provstate'],
                "city": row['city'],
                "coordinates": {"latitude": row['latitude'], "longitude": row['longitude']},
            },
            casualties={
                "killed": row['nkill'],
                "killed_terrorists": row['nkillter'],
                "wounded": row['nwound'],
                "wounded_terrorists": row['nwoundte'],
            },
            attack={
                "type": row['attacktype1_txt'],
                "target": {"type": row['targtype1_txt']},
            },
            attackers={
                "primary_group": row['gname'],
                "secondary_group": row['gname2'],
                "tertiary_group": row['gname3'],
                "perpetrators": row['nperps'] if row['nperps'] != -99 else 0,
                "captured": row['nperpcap'] if row['nperpcap'] != -99 else 0,
            },
        )
        return event.model_dump()
    except Exception as e:
        print(f"Error processing row: {row['eventid']}, Error: {e}")
        return None
