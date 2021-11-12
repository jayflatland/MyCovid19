import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
from county_to_county_code_map import county_to_county_code_map
import matplotlib as mpl

# %%

cases = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
deaths = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")

# %%
county_ids = pd.DataFrame(county_to_county_code_map)
county_ids = county_ids.rename(columns={"code": "County_ID"})

# %%

df = cases
df = df.rename(columns={"Combined_Key": "County"})
df = df.merge(county_ids, how='left', on='County')
df = df[df['County_ID'].notnull()]
df = df.set_index('County_ID')
df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))

# %%
def colorFader(mix):
    mix = min(mix, 1.0)
    mix = max(mix, 0.0)
    c1='white'
    c2='red'
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

# %%

final = df.iloc[-1]
final = final / final.max()

#plt.plot(list(final))

fd = open('animator.js', 'w')

print("function do_animator() {", file=fd)
for county_id, x in final.items():
    cc = colorFader(x)
    print(f'    $("#{county_id}").css("fill", "{cc}");', file=fd)

print("}", file=fd)
fd.close()
