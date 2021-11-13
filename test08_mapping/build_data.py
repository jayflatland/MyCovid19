#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
from county_to_county_code_map import county_to_county_code_map
import matplotlib as mpl
import matplotlib.cm

# %%

df = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")

# %%
county_ids = pd.DataFrame(county_to_county_code_map)
county_ids = county_ids.rename(columns={"code": "County_ID"})

# %%

df = df.rename(columns={"Combined_Key": "County"})
df = df.merge(county_ids, how='left', on='County')
df = df[df['County_ID'].notnull()]
df = df.set_index('County_ID')
df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))
df = df.fillna(0.0)
df = df.diff()
df_u1 = df.rolling(7*5).mean()
df_u2 = df.rolling(7*8).mean()
df_s2 = df.rolling(7*8).std()
df = (df_u1 - df_u2) / df_s2 / 0.6

#plt.plot(df[df.columns[:25]])

df = df * 0.5 + 0.5
df = df.clip(lower=0.0, upper=1.0)

# %%

colormap = matplotlib.cm.get_cmap('coolwarm')

fd = open('data_by_county.js', 'w')

fd.write("var date_by_idx = [")
for dt in list(df.index):
    dt = str(dt)[:10]
    fd.write(f'"{dt}", ')
fd.write("];\n")


print("var color_by_county_id = {", file=fd)
cols = sorted(df.columns)
for i, county_id in enumerate(cols):
    pct = 100 * i / len(cols)
    print(f"{pct:.1f}% done")
    fd.write(f'"{county_id}": [')
    rows = list(df[county_id])
    for x in rows:
        r, g, b, a = colormap(x, bytes=True)
        fd.write(f'"#{r:02x}{g:02x}{b:02x}",')
    fd.write("],\n")

print("};", file=fd)
fd.close()
