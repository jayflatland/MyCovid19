import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
#df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")
#df = df[df['Country_Region'] == 'US']
#df = df[df['Province/State'] == 'Johnson County, KS']
counties = [
    # Mom/Dad
    'Mille Lacs, Minnesota, US',     # Milaca
    'Kanabec, Minnesota, US',        # Mora
    'Benton, Minnesota, US',         # Foley
    'Morrison, Minnesota, US',       # Little Falls
    'Crow Wing, Minnesota, US',      # Brainerd
    # 'Stearns, Minnesota, US',        # St Cloud

    # Brian
    # 'Steele, Minnesota, US',         # Ellendale

    # Jay
    # 'Johnson, Kansas, US',      # Olathe
    # 'Wyandotte, Kansas, US',
    # 'Leavenworth, Kansas, US',
    # 'Jackson, Missouri, US', # KC
    # 'Platte, Missouri, US',
    # 'Clay, Missouri, US',
]
df = df.rename(columns={"Combined_Key": "County"})
#d = sorted(df.County)
df = df[df['County'].isin(counties)]
df = df.set_index('County')
#Mille Lacs, Minnesota, US
# %%

#df = df.set_index('Province/State')
df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))
df_d = df.diff()
df_du = df_d.rolling(7).mean()
#df.columns = ['v']
#df['d'] = df.diff()
#df['u'] = df['d'].rolling(7).mean()

#df.plot()
df_du.plot()

# %%
#plt.figure()
#plt.title("Mille Lacs County Covid Cases")
#plt.plot(df)
#plt.plot(df['u'], label='7 Day Moving Average')

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
