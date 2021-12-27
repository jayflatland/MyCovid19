#!/usr/bin/env python

import pandas as pd
from county_to_county_code_map import county_to_county_code_map
import matplotlib.cm
from state_abbrevs import state_to_abbrev, abbrev_to_state

# %%
county_ids = pd.DataFrame(county_to_county_code_map)
county_ids = county_ids.rename(columns={"code": "County_ID"})

# %%

populations = pd.read_csv("co-est2019-alldata.csv")
populations = populations[['STNAME', 'CTYNAME', 'POPESTIMATE2019']]

#Prince of Wales-Hyder, Alaska, US
county_pops = []
for stname, ctyname, population in zip(populations['STNAME'], populations['CTYNAME'], populations['POPESTIMATE2019']):
    #ctyname = ctyname.replace(" County", "")
    county = f"{ctyname}, {stname}, US"
    county_pops.append({"County": county, "Population": population})
county_pops = pd.DataFrame(county_pops)

populations = county_ids.merge(county_pops, how='left', on='County')
populations = populations.set_index('County_ID')
populations = populations[['Population']]

# %%

cases = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")

#HACK TEST - deaths
#cases = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")
#del cases['Population']

cases = cases.rename(columns={"Combined_Key": "County"})
cases = cases.merge(county_ids, how='left', on='County')
cases = cases[cases['County_ID'].notnull()]
cases = cases.set_index('County_ID')
cases = cases[cases.columns[11:]]
#cases = cases.join(populations, how='left')
#cases[cases.columns[:-1]] / cases['Population']
#cases
# %%

"""
polk, fl (c12105) - population = 724777
"""

#cases_per_captia = cases / populations
#cases_per_captia['c12105']
#populations['c12105']
#cases['c12105']

cases = cases.T

cases = cases.set_index(pd.to_datetime(cases.index))
cases = cases.fillna(0.0)

#cases_per_captia = cases_per_captia.T
#cases_per_captia = cases_per_captia.set_index(pd.to_datetime(cases.index))
#cases_per_captia = cases_per_captia.fillna(0.0)

#plt.plot(sorted(cases.diff().diff().min()))

# %%
new_cases = cases.diff().clip(lower=0.0)
#new_cases_per_captia = cases_per_captia.diff().clip(lower=0.0)
#contagious_people_per_capita = new_cases_per_captia.rolling(14).sum()

chart_data = new_cases
chart_data = chart_data.rolling(7).mean()
chart_data = chart_data.fillna(0.0)

# fast_weeks = 5
# slow_weeks = 8
# fast_weeks = 2
# slow_weeks = 8
# u1 = new_cases.rolling(7*fast_weeks).mean()
# u2 = new_cases.rolling(7*slow_weeks).mean()
# s2 = new_cases.rolling(7*slow_weeks).std()
# heat = (u1 - u2) / s2

#u1 = new_cases.rolling(7*4).mean()
#heat = u1 - u1.shift(7)
#heat = heat / heat.rolling(56).std()

#u1 = new_cases.rolling(7).mean()
#heat = (u1 - u1.rolling(60).mean()) / u1.rolling(60).std()

u1 = new_cases.rolling(7).mean()
heat = (u1 - u1.mean()) / u1.std()

#chart_data = heat.fillna(0.0)

if 0:
    import matplotlib.pylab as plt
    plt.plot(heat[heat.columns[:25]])

range_scaler = 4.0
heat = heat.fillna(0.0)
heat = heat / range_scaler * 0.5 + 0.5
heat = heat.clip(lower=0.0, upper=1.0)



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
cols = sorted(chart_data.columns)
for i, county_id in enumerate(cols):
    pct = 100 * i / len(cols)
    # print(f"{pct:.1f}% done")
    fd.write(f'"{county_id}": [')
    rows = list(chart_data[county_id])
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
