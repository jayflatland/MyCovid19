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

cases = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
deaths = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")

# %%
county_ids = pd.DataFrame(county_to_county_code_map)
county_ids = county_ids.rename(columns={"code": "County_ID"})

# %%

df = cases
df = df.rename(columns={"Combined_Key": "County"})
df = df.merge(county_ids, how='left', on='County')
df = df[df['County_ID'].notnull()]
df = df.set_index('County_ID')
df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))
df = df.fillna(0.0)
df7 = df.rolling(7).mean()
df28 = df.rolling(8).mean()
df = df7 - df28
#df = np.log(df)

#df = df / df.max()  #normalize by county max
df = (df.T / df.max(axis=1).T).T  #normalize by date max

#plt.plot(df[df.columns[:25]])

# %%

m = matplotlib.cm.get_cmap('Reds')

fd = open('data_by_county.js', 'w')

fd.write("var date_by_idx = [")
for dt in list(df.index):
    dt = str(dt)[:10]
    fd.write(f'"{dt}", ')
fd.write("];\n")


print("var color_by_county_id = {", file=fd)
for county_id in sorted(df.columns):
    print(county_id)
    fd.write(f'"{county_id}": [')
    rows = list(df[county_id])
    for x in rows:
        r, g, b, a = m(x, bytes=True)
        fd.write(f'"#{r:02x}{g:02x}{b:02x}",')
    fd.write("],\n")

print("};", file=fd)
fd.close()
