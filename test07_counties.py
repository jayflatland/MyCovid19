import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
#df = df[df['Country_Region'] == 'US']
#df = df[df['Province/State'] == 'Johnson County, KS']
df = df[df['Combined_Key'] == 'Mille Lacs, Minnesota, US']
#df = df[df['Combined_Key'] == 'Stearns, Minnesota, US']
#df = df[df['Combined_Key'] == 'Steele, Minnesota, US']

#Mille Lacs, Minnesota, US

#df = df.set_index('Province/State')
df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))
df.columns = ['v']
df['d'] = df.diff()
df['u'] = df['d'].rolling(7).mean()

# %%
plt.figure()
plt.title("Mille Lacs County Covid Cases")
plt.plot(df['d'], label='Daily New Cases')
plt.plot(df['u'], label='7 Day Moving Average')
plt.legend()
plt.show()

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



# df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-23-2020.csv")
# df = df[df['Province_State'] == 'Kansas']

# # %%

# df = pd.read_csv("../../Opensource/COVID-19/who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/who_covid_19_sit_rep_time_series.csv")

# df = df.set_index(list(df.columns[:3])).T
