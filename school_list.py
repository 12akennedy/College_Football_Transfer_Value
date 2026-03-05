# python school_list.py
import pandas as pd
import numpy as np
import requests

api_key = key #set outside script
url = "https://api.collegefootballdata.com/teams"


df = pd.concat(
    pd.DataFrame(
        requests.get(
            url,
            params={"year": y},
            headers={"Authorization": f"Bearer {api_key}"}
        ).json()
    ).assign(year = y)
    for y in range(2022, 2027)  # 2021 to 2026 inclusive
)
# define power conferences
p4 = ['Big Ten','Big 12','SEC','ACC','Pac-12']
# only keep FBS schools
school_list = df[df['classification'] == 'fbs']
# Define power schools
school_list['conference_type'] = np.where(
    (school_list['conference'] == 'Pac-12') & (school_list['year'] > 2023), "g6",
    np.where(
        (school_list['school'] == "Notre Dame") | (school_list['conference'].isin(['Big Ten','Big 12','SEC','ACC'])) | 
        ((school_list['conference'] == 'Pac-12') & (school_list['year'] <= 2023)),
        "p4",
        "g6"
    )
)
# keep basic data
school_list = school_list[['year','school','conference','conference_type']]
#Export
school_list.to_csv("historical.csv", index = False)