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
#df.groupby('Country_Region')[['Confirmed', 'Deaths']].sum()
df2 = df.groupby('Province_State')[['Confirmed', 'Deaths']].sum()
