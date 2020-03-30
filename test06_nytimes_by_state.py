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

d = df.pivot_table(index='date', columns='state', values='cases')
d['Total'] = d.sum(axis=1)
dd = d.diff()
dl = d * 0 + np.log(d)

dr = dd / d * 100.0

# %%
plt.figure()
plt.title("Daily Cases Increase Percent")
cols = [
    'New York',
    'California',
    'Michigan',
    'Kansas',
    'Missouri',
    'Total',
]
#cols = list(d)

for c in cols:
    plt.plot(dr[c].rolling(3).mean(), label=c)
plt.legend()
plt.show()

# %%

#plt.figure()
#plt.plot(d['New York'], dd['New York'])

## %%
#plt.figure()
#plt.plot(d['Total'], dd['Total'])
#
## %%
#plt.figure()
#plt.plot(dl['New York'].diff())
#
## %%
#plt.figure()
#plt.plot(dl['Total'].diff())
