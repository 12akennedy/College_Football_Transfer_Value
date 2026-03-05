# python transfer_portal_pull.py

import os, requests, pandas as pd

# 1) Get your API key from an environment variable
api_key = key #set outside script
url = "https://api.collegefootballdata.com/player/portal"

df = pd.concat(
    pd.DataFrame(
        requests.get(
            url,
            params={"year": y},
            headers={"Authorization": f"Bearer {api_key}"}
        ).json()
    )
    for y in range(2022, 2027)  # 2021 to 2026 inclusive
)
 # Make a copy of the concatenated DataFrame
df.to_csv("Transfer_Portal_data.csv", index = False)
