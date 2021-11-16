#!/usr/bin/env python

import pandas as pd
from county_to_county_code_map import county_to_county_code_map
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
df = df.rolling(7).mean()
df = (df - df.mean())/df.std()
#u1 = df.rolling(7*5).mean()
#u2 = df.rolling(7*8).mean()
#s2 = df.rolling(7*8).std()
#df = (u1 - u2) / s2
df = df.fillna(0.0)

# %%

import sklearn.cluster

X = df.T
cluster = sklearn.cluster.KMeans(n_clusters=8).fit(X)
#cluster = sklearn.cluster.DBSCAN(eps=3, min_samples=600).fit(X)

# %%

colormap = matplotlib.cm.get_cmap('Paired')
def cc(i):
    r, g, b, a = colormap(i, bytes=True)
    return f'#{r:02x}{g:02x}{b:02x}'

fd = open('gendata.js', 'w')

fd.write("var color_by_cluster = {\n")
for county_id, lbl in zip(df.columns, cluster.labels_):
    fd.write(f'    {county_id}: "{cc(lbl)}",\n')
fd.write("};\n")
fd.close()

