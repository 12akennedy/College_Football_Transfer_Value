# python transfer_data_complete.py

import pandas as pd
import numpy as np
import os


# import transfer portal data and schoo list
df = pd.read_csv("Transfer_Portal_data.csv")

# Remove athlets who withdrew from the portal or stayed at the same school.
df = df[~((df['origin'] == df['destination']) | (df['eligibility'] == 'Withdrawn'))]
# Also only keep those who had a destination
df = df[~df['destination'].isna()]

school = pd.read_csv("School_List.csv")

#Merge data to find the origin conference and type. year adjustment is for those schools that
# recently joined the FBS
df = pd.merge(df, school, left_on = "origin", right_on = "school", how = 'left')

# remove extra columns
df = df.drop(columns=['transferDate','eligibility','school'])
df = df.rename(columns={'conference': 'origin_conf'})
df = df.rename(columns={'conference_type': 'origin_type'})
# repeate for desination, or where they ended up

df = pd.merge(df, school, left_on = "destination", right_on = "school", how = "left")
df = df.rename(columns={'conference': 'destination_conf'})
df = df.rename(columns={'conference_type': 'destination_type'})
# remove extra columns
df = df.drop(columns='school')

#Account for dII or dIII transfers
df.loc[df["origin_conf"].isna() & df["origin"].notna(), "origin_conf"] = "lower_division"
df.loc[df["origin_type"].isna() & df["origin"].notna(), "origin_type"] = "lower_division"
df.loc[df["destination_conf"].isna() & df["destination"].notna(), "destination_conf"] = "lower_division"
df.loc[df["destination_type"].isna() & df["destination"].notna(), "destination_type"] = "lower_division"

# adjust positions to typical listings
df['position'] = df['position'].replace({
    'PRO': 'QB',
    'OLB': 'LB',
    'OLB': 'LB',
    'DT': 'DL',
    'ILB': 'LB',
    'OG': 'IOL',
    'WDE': 'EDGE',
    'SDE': 'DL',
    'DUAL': 'QB',
    'OC': 'IOL',
    'APB': 'RB'
})

df['Name'] = df['firstName'] + ' ' + df['lastName']
df = df.drop(columns=['firstName','lastName'])

df.to_csv("transfer_22_26.csv", index = False)