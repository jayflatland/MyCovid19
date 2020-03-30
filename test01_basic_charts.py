import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

#df = pd.read_csv("/home/jay/Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv")
#df = df[df['Country/Region'] == 'US']

dfs = []
# from https://github.com/CSSEGISandData/COVID-19.git
basepath = "../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"
for e in sorted(os.listdir(basepath)):
    if e.endswith(".csv"):
        print(e)
        date = e.replace(".csv", "")
        df = pd.read_csv(f"{basepath}/{e}")
        df['date'] = date
        dfs.append(df)
# %%
df = pd.concat(dfs, sort=False)
df['date'] = pd.to_datetime(df['date'])
#df = df.set_index('date').sort_index()

# %%


#df.pivot_table(index='date', columns='Country/Region', values='Confirmed').plot()

df2 = df.groupby(('Country/Region', 'date'))[['Confirmed', 'Deaths', 'Recovered']].sum()
df2 = df2.reset_index()

df_cnt = df2.pivot_table(index='date', columns='Country/Region', values='Confirmed').ffill().fillna(0.0)
df_rec = df2.pivot_table(index='date', columns='Country/Region', values='Recovered').ffill().fillna(0.0)
df_ded = df2.pivot_table(index='date', columns='Country/Region', values='Deaths').ffill().fillna(0.0)

df_act = df_cnt - (df_rec + df_ded)
df_dedrate = df_ded / df_cnt * 100.0

X = df_cnt.max(axis=0)
major_outbreaks = list(X[X > 200].index)
all_countries = list(df['Country/Region'].unique())

#focus_countries = all_countries[:]
#focus_countries = major_outbreaks
#focus_countries.remove('Mainland China')
focus_countries = ['US']
# focus_countries = ['US', 'Iran', 'Italy']
focus_countries = ['Italy']
focus_countries = ['Mainland China']
# focus_countries = ['South Korea']
focus_countries = ['Mainland China', 'South Korea', 'Italy', 'Iran', 'US']
focus_countries = ['South Korea', 'Italy', 'Iran', 'US']


# %%
if 0:
    pass
    # %%
    d = df_cnt[focus_countries]
    # d = d.sum(axis=1)
    d = d.diff()
    d = (d / d.shift(1) - 1.0) * 100.0
    #d.rolling(7).mean().plot(title='Growth Percent per Day')
    plt.figure()
    plt.title('Growth Rate (Ratio per Day)')
    plt.plot(d)
    plt.ylim(0, 150)
    plt.show()


# %%
if 0:
    pass
    # %%
    
    df_dedrate[focus_countries].plot(title='Mortality Rate')
    
    df_act[focus_countries].plot(title='Active Cases (Confirmed minus Dead/Recovered)')
    
    df_cnt[focus_countries].plot(title='Count')
    df_cnt[focus_countries].diff().plot(title='New Cases per Day', kind='bar')

    df_ded[focus_countries].plot(title='Deaths')
    df_rec[focus_countries].plot(title='Recoveries')

    df_ded[focus_countries].diff().plot(title='Deaths/Day')
    df_ded[focus_countries].diff().diff().plot(title='Deaths/Day/Day')
    df_ded[focus_countries].diff().diff().ewm(alpha=0.2).mean().plot(title='Deaths/Day/Day')
    
# %%
if 0:
    pass
    # %%
    # from https://github.com/jihoo-kim/Coronavirus-Dataset.git
    df = pd.read_csv('../../../Opensource/Coronavirus-Dataset/patient.csv')
