import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

# from https://github.com/nytimes/covid-19-data.git
#df = pd.read_csv('../../Opensource/covid-19-data/us-states.csv')
df = pd.read_csv('../../Opensource/covid-19-data/us-counties.csv')

df['date'] = pd.to_datetime(df['date'])
#df = df.set_index(pd.to_datetime(df['date'])).sort_index()


# %%
d = df.copy()
if 1: # by state
    d = df.pivot_table(index='date', values='cases', columns='state')
    high_counts = d.loc[Timestamp("2020-06-10")] > 300
else:  # by county
    #d = d[d['state'] == 'Arizona']
    #d = d[d['state'] == 'South Carolina']
    #d = d[d['state'] == 'Florida']
    high_counts = d.loc[Timestamp("2020-06-10")] > 10
    d = d.pivot_table(index='date', values='cases', columns='county')
d = d.fillna(0.0)
d = d.diff()
d = d.rolling(14).mean()
d = d[Timestamp("2020-03-15"):]

## %%
old_mean = d[Timestamp("2020-05-10") : Timestamp("2020-05-22")].mean()
tst = d.loc[Timestamp("2020-06-10")] / old_mean
tst = tst[high_counts]
tst = tst.sort_values(ascending=False)
print(tst)

# %%
"""
state
Arizona           2.506397
South Carolina    2.348092
Utah              2.028935
North Carolina    2.022837
Florida           1.562613
California        1.527699
Alabama           1.501755
Texas             1.399262
"""

states = [
    # Legit Second Waves
    'Arizona',
    'South Carolina',
    'Utah',
    'North Carolina',
    'Florida',
    'Texas',

#    'Alabama',
#    'Arkansas',
    #'North Carolina',

#    'Washington',
    # Same Old Trend
#    'Michigan',
#    'Texas',
#    'California',
#    'Mississippi',

    #'Kansas',
    #'Minnesota',
]

plt.figure()
plt.title("Daily New Cases, by State (14 day Moving Average)")
for state in states:
    #plt.plot(d[state] / d[state].sum(), label=state)
    plt.plot(d[state], label=state)
plt.legend()
plt.show()

