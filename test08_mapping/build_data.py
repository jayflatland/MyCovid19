#!/usr/bin/env python

import pandas as pd
from county_to_county_code_map import county_to_county_code_map
import matplotlib.cm

# %%

df = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")

# %%
county_ids = pd.DataFrame(county_to_county_code_map)
county_ids = county_ids.rename(columns={"code": "County_ID"})

# %%

df = df.rename(columns={"Combined_Key": "County"})
df = df.merge(county_ids, how='left', on='County')
df = df[df['County_ID'].notnull()]
df = df.set_index('County_ID')
df = df[df.columns[11:]].T
df = df.set_index(pd.to_datetime(df.index))
df = df.fillna(0.0)

new_cases = df.diff()

new_cases_smoothed = new_cases
new_cases_smoothed = new_cases_smoothed.rolling(7).mean()
new_cases_smoothed = new_cases_smoothed.fillna(0.0)

u1 = new_cases.rolling(7*5).mean()
u2 = new_cases.rolling(7*8).mean()
s2 = new_cases.rolling(7*8).std()
heat = (u1 - u2) / s2

#import matplotlib.pylab as plt
#DBG plt.plot(heat[heat.columns[:25]])

heat = heat / 0.6 * 0.5 + 0.5
heat = heat.clip(lower=0.0, upper=1.0)
heat = heat.fillna(0.0)

# %% scale to lookup table index
print("Building color lut...")
lut_cnt = 65536
lut_max = lut_cnt - 1
heat = (heat * lut_max).astype(int)

colormap = matplotlib.cm.get_cmap('coolwarm')
def cc(x):
    x = float(x) / lut_max
    r, g, b, a = colormap(x, bytes=True)
    return f'#{r:02x}{g:02x}{b:02x}'
cc_lut = [cc(x) for x in range(lut_cnt)]

# %%


fd = open('gendata.js', 'w')

fd.write("var date_by_idx = [")
for dt in list(heat.index):
    dt = str(dt)[:10]
    fd.write(f'"{dt}", ')
fd.write("];\n")

print("Building new cases table...")
print("var new_cases_by_county_id = {", file=fd)
cols = sorted(new_cases_smoothed.columns)
for i, county_id in enumerate(cols):
    pct = 100 * i / len(cols)
    # print(f"{pct:.1f}% done")
    fd.write(f'"{county_id}": [')
    rows = list(new_cases_smoothed[county_id])
    for x in rows:
        fd.write(f'{x},')
    fd.write("],\n")

print("};", file=fd)

print("Building heatmap table...")
print("var color_by_county_id = {", file=fd)
cols = sorted(heat.columns)
for i, county_id in enumerate(cols):
    pct = 100 * i / len(cols)
    # print(f"{pct:.1f}% done")
    fd.write(f'"{county_id}": [')
    rows = list(heat[county_id])
    for x in rows:
        cc = cc_lut[x]
        fd.write(f'"{cc}",')
    fd.write("],\n")

print("};", file=fd)

fd.close()
