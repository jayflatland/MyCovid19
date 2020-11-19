import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

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
#    'Johnson, Kansas, US',      # Olathe
#    'Wyandotte, Kansas, US',
#    'Leavenworth, Kansas, US',
#    'Jackson, Missouri, US', # KC
#    'Platte, Missouri, US',
#    'Clay, Missouri, US',
]


# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
df = df.rename(columns={"Combined_Key": "County"})
df = df[df['County'].isin(counties)]
df = df.set_index('County')

# %%

df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))
df_d = df.diff()
df_du = df_d.rolling(7).mean()

df_du.plot(title="Daily New Cases (7 day MA)")

# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")
df = df.rename(columns={"Combined_Key": "County"})
df = df[df['County'].isin(counties)]
df = df.set_index('County')

# %%

df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))
df_d = df.diff()
df_du = df_d.rolling(7).mean()
df.plot(title="Deaths")
#df_d.plot(title="Daily Deaths")

