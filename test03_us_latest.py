import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-24-2020.csv")

df = df[df['Country_Region'] == 'US']
df.groupby('Country_Region')[['Confirmed', 'Deaths']].sum()
df2 = df.groupby('Province_State')[['Confirmed', 'Deaths']].sum()

# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

df = df[df['Country/Region'] == 'US']
df.T

# %%


df = pd.read_csv("../../Opensource/COVID-19/data/cases_time.csv")
df = df[df['Country_Region'] == 'US']
df = df.set_index(pd.to_datetime(df['Last_Update']))
df['Percent Increase'] = (df['Delta_Confirmed'] / df['Confirmed']) * 100.0
df = df[Timestamp("2020-03-02"):]
#df.groupby('Country_Region')[['Confirmed', 'Deaths']].sum()
plt.figure()
plt.title("Percentage Increase in US per Day")
plt.plot(df['Percent Increase'])
plt.show()

