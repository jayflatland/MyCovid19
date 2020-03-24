import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv")
df = df[df['Country/Region'] == 'US']
df = df[df['Province/State'] == 'Johnson County, KS']
df = df.set_index('Province/State')
df = df[df.columns[3:]].T


plt.plot(df)

# dfs = []
# # from https://github.com/CSSEGISandData/COVID-19.git
# basepath = "../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"
# for e in sorted(os.listdir(basepath)):
#     if e.endswith(".csv"):
#         print(e)
#         date = e.replace(".csv", "")
#         df = pd.read_csv(f"{basepath}/{e}")
#         df['date'] = date
#         dfs.append(df)
# # %%
# df = pd.concat(dfs, sort=False)
# df['date'] = pd.to_datetime(df['date'])
# #df = df.set_index('date').sort_index()

# %%



df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-23-2020.csv")
df = df[df['Province_State'] == 'Kansas']

# %%

df = pd.read_csv("../../Opensource/COVID-19/who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/who_covid_19_sit_rep_time_series.csv")

df = df.set_index(list(df.columns[:3])).T
