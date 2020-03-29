import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

# from https://github.com/nytimes/covid-19-data.git

df = pd.read_csv('../../Opensource/covid-19-data/us-states.csv')
# df = pd.read_csv('../../Opensource/covid-19-data/us-counties.csv')
df['date'] = pd.to_datetime(df['date'])
# df = df.set_index(pd.to_datetime(df['date'])).sort_index()

# %%

d = df.pivot_table(index='date', columns='state', values='deaths')
# d[d.max(axis=0) > 100]
dlog = d * 0 + np.log10(d)
dlog.plot()

dtotal = d.fillna(0.0).sum(axis=1)
dlogtotal = dtotal * 0 + np.log10(dtotal)
dlogtotal.plot()
dtotal.plot()
((dtotal / dtotal.shift(1) - 1.0) * 100.0).plot()

plt.figure()
plt.semilogy(d)
plt.legend()
plt.show()

d2 = d.copy()
d2 = d2 * np.where(d2 < 20, np.nan, 1.0)

d3 = (d2 / d2.shift(1) - 1.0) * 100
d4 = d3.rolling(3).mean()

d5 = d2 - d2.shift(1)

# %%

df = df[df['state'] == 'New York']
df = df[df['county'] == 'New York City']

plt.figure()
plt.plot(df['cases'])
plt.show()

