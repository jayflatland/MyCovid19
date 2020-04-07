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

r, c = 2, 2
fig, axs = plt.subplots(r, c, figsize=(18, 18), sharex=True)
if r == 1 and c == 1: axs = [axs]
elif r == 1 or c == 1:  axs = list(axs)
else: axs = [axs[i, j] for j in range(c) for i in range(r)]  # flatten


d = df.pivot_table(index='date', columns='state', values='cases')
d['Total'] = d.sum(axis=1)
dd = d.diff()
dr = dd / d * 100.0

ddr = (dd / dd.shift(1) - 1) * 100.0

cols = [
    'New York',
    'California',
    #'Michigan',
    #'Kansas',
    #'Missouri',
    'Texas',
    'Florida',
    'Total',
]

#plt.sca(axs.pop(0))
#plt.title("Cases")
#
#for c in cols:
#    plt.plot(d[c].rolling(3).mean(), label=c)
#    # plt.plot(dr[c], label=c)
#plt.legend()
#plt.xticks(rotation=45)
#plt.subplots_adjust(bottom=0.15)


#plt.sca(axs.pop(0))
#plt.title("Daily Cases Increases")
#
#for c in cols:
#    plt.plot(dd[c].rolling(3).mean(), label=c)
#    # plt.plot(dr[c], label=c)
#plt.legend()
#plt.xticks(rotation=45)
#plt.subplots_adjust(bottom=0.15)



plt.sca(axs.pop(0))
plt.title("Daily Cases Increase Percent (3 day MA)")

for c in cols:
    plt.plot(dr[c].rolling(3).mean(), label=c)
    # plt.plot(dr[c], label=c)
plt.legend()
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.15)



plt.sca(axs.pop(0))
plt.title("Daily New Cases Percent Change")# (3 day MA)")

for c in cols:
    # plt.plot(ddr[c].rolling(3).mean(), label=c)
    plt.plot(ddr[c], label=c)
plt.legend()
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.15)

# %%

d = df.pivot_table(index='date', columns='state', values='deaths')
d['Total'] = d.sum(axis=1)
dd = d.diff()
dr = dd / d * 100.0

cols = [
    'New York',
    'California',
    # 'Michigan',
    # 'Kansas',
    # 'Missouri',
    # 'Texas',
    # 'Florida',
    'Total',
]

#plt.sca(axs.pop(0))
#plt.title("Deaths")
#
#for c in cols:
#    plt.plot(d[c].rolling(3).mean(), label=c)
#    # plt.plot(dr[c], label=c)
#plt.legend()
#plt.xticks(rotation=45)
#plt.subplots_adjust(bottom=0.15)


#plt.sca(axs.pop(0))
#plt.title("Daily Deaths Increases")
#
#for c in cols:
#    plt.plot(dd[c].rolling(3).mean(), label=c)
#    # plt.plot(dr[c], label=c)
#plt.legend()
#plt.xticks(rotation=45)
#plt.subplots_adjust(bottom=0.15)


plt.sca(axs.pop(0))


plt.sca(axs.pop(0))
plt.title("Daily Deaths Increase Percent (3 day MA)")

for c in cols:
    plt.plot(dr[c].rolling(3).mean(), label=c)
    # plt.plot(dr[c], label=c)
plt.legend()
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.15)


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
