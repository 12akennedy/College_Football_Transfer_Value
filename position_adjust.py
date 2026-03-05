# python position_adjust.py

import pandas as pd
import numpy as np
import os
df = pd.read_csv("transfer_22_26.csv")

df['net_rating'] = np.where(df['rating'].isna(), -.5, df['rating'])

#Add adjustment for QB data
qb = pd.read_csv("qb_data.csv", encoding = "latin1")

# Add 1 to year to help merge
qb['season'] = qb['season'] + 1
qb['Player'] = qb['Player'].str.replace(".",  "", regex=False)
qb = qb[['season','Player','Att']]
# Fix names
df['Name'] = df['Name'].str.replace(".",  "", regex=False)
 # Merge together
df = df.merge(qb, left_on = ['season','Name'], right_on = ['season','Player'], how = "left")
#df = df[['season','Name','position','origin','origin_conf','origin_type','destination','destination_conf','destination_type','rating','stars','Att']]

df['net_rating'] = np.where(
    df['position'] != "QB",
    df['net_rating'],
    df['net_rating'] * np.minimum(df['Att']/100,1.3)
)
df['transfer_value'] = (df['stars'] + df['net_rating'])**2

df = df[['season','Name','position','origin','origin_conf','origin_type','stars','rating','Att','destination','transfer_value']]
df = df.sort_values('transfer_value', ascending=False)
# df.head()
df.to_csv("player_value.csv", index = False)