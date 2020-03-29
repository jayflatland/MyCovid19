import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

# from https://github.com/nytimes/covid-19-data.git

# df = pd.read_csv('../../Opensource/covid-19-data/us-states.csv')
df = pd.read_csv('../../Opensource/covid-19-data/us-counties.csv')
df['date'] = pd.to_datetime(df['date'])
# df = df.set_index(pd.to_datetime(df['date'])).sort_index()

# %%

d = df.pivot_table(index='date', columns=('state', 'county'), values='cases')
# d[d.max(axis=0) > 100]

majors = []
for c in d:
    if d[c].values[-1] > 600 or c == ('Kansas', 'Johnson'):
        majors.append(c)

d2 = d[majors]
d2 = d2 * np.where(d2 < 20, np.nan, 1.0)
d2 = d2.dropna(how='all')

d3 = (d2 / d2.shift(1) - 1.0) * 100
d4 = d3.rolling(3).mean()

d5 = d2 - d2.shift(1)

# %%

df = df[df['state'] == 'New York']
df = df[df['county'] == 'New York City']

plt.figure()
plt.plot(df['cases'])
plt.show()

