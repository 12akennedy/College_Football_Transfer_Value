# python transfer_grades.py

import pandas as pd, numpy as np, os

df = pd.read_csv("player_value.csv")

df =df[~df['origin_type'].str.contains('lower_division')]

df = df.groupby(['season','origin','origin_conf','origin_type'])['transfer_value'].sum().reset_index()
df = df.sort_values('transfer_value', ascending=False)
df['transfer_value'] = df['transfer_value'] * -1


df_26 = df[df['season'] == 2026]
grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

# Overall grade
df_26['Overall_Grade'] = pd.qcut(df_26['transfer_value'].rank(method='first', ascending=False),
                                  q=len(grades), labels=grades)

# Grade within conf_type
# default to "NA"
df_26["Conference_Grade"] = "NA"

# mask out independents
mask = df_26["Conference_Grade"] != "FBS Independents"

# compute grades only for non-independents
df_26.loc[mask, "Conference_Grade"] = (
    df_26.loc[mask]
        .groupby("origin_conf")["transfer_value"]
        .rank(method="first", ascending=False)
        .pipe(lambda x: pd.qcut(x, q=len(grades), labels=grades))
)

# Grade within conf
df_26['School_Tier_Grade'] = df_26.groupby('origin_type')['transfer_value'] \
                           .rank(method='first', ascending=False) \
                           .pipe(lambda x: pd.qcut(x, q=len(grades), labels=grades))
df_26['adjusted_value'] = df_26['transfer_value'] * -1
df_26.columns = ['Year','School','Conference','School Type','Raw Score','Overall Grade','Conference Grade','School Type Grade','Transfer Value Lost']

df_26.to_csv("team_grade.csv", index = False)