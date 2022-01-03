import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')

# %%

df = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
df = df.rename(columns={"Combined_Key": "County"})

all_counties = list(df['County'])

focus_counties = [
    "New York, New York, US",
    "Cook, Illinois, US",
    "Honolulu, Hawaii, US",
    "Cuyahoga, Ohio, US",
    "Miami-Dade, Florida, US",
    "Fulton, Georgia, US",
]

#focus_counties += filter(lambda e : e.endswith(", New Jersey, US"), all_counties)
##focus_counties += filter(lambda e : e.endswith(", New York, US"), all_counties)
##focus_counties += filter(lambda e : e.endswith(", Florida, US"), all_counties)

#focus_counties_label = "Hardest Hit"#"NYC, NJ, Miama, Cleveland, and Chicago"
focus_counties_label = "NYC, Chicago, Miami, Atlanta, Cleveland, Honolulu"#"NYC, NJ, Miama, Cleveland, and Chicago"

# focus_counties = []
# focus_counties_label = "All US"

# %%

cases = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
cases = cases.rename(columns={"Combined_Key": "County"})
if len(focus_counties) > 0: cases = cases[cases['County'].isin(focus_counties)]
cases = cases.set_index('County')
cases = cases[cases.columns[11:]].T
cases = cases.set_index(pd.to_datetime(cases.index))

deaths = pd.read_csv("../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")
deaths = deaths.rename(columns={"Combined_Key": "County"})
if len(focus_counties) > 0: deaths = deaths[deaths['County'].isin(focus_counties)]
deaths = deaths.set_index('County')
deaths = deaths[deaths.columns[11:]].T
deaths = deaths.set_index(pd.to_datetime(deaths.index))


# %%

total_new_cases = cases.sum(axis=1).diff().rolling(7).mean()
total_new_deaths = deaths.sum(axis=1).diff().rolling(7).mean()

df = pd.DataFrame(dict(new_cases=total_new_cases, new_deaths=total_new_deaths))

# %%

# if len(focus_counties) <= 3:
#     plt.figure()
#     plt.title(f"New Cases - {focus_counties}")
#     plt.plot(df['new_cases'])
#     plt.show()

# %%
"""
###############################################################################
https://www.worldometers.info/coronavirus/coronavirus-death-rate/
A study of these cases found that the median days from first symptom to death 
were 14 (range 6-41) days, and tended to be shorter among people of 70 year old
or above (11.5 [range 6-19] days) than those with ages below 70 year old (20 
[range 10-41] days.
"""
# 14 is from research
# 28 fits well
avg_days_from_symptoms_to_death = 28
#df['new_deaths_delayed'] = df['new_deaths'].shift(avg_days_from_symptoms_to_death)
df['new_cases_delayed'] = df['new_cases'].shift(avg_days_from_symptoms_to_death)
df['mortality_rate'] = df['new_deaths'] / df['new_cases_delayed']

#df = df[Timestamp("2021-07-01"):]

fig, axs = plt.subplots(3, 1, sharex=True)
plt.suptitle(focus_counties_label)
axs[0].plot(df['new_cases'], label="Cases")
axs[0].plot(df['new_cases_delayed'], label=f"Cases (delayed {avg_days_from_symptoms_to_death}d)")
axs[0].legend()
axs[1].plot(df['new_deaths'], label="Deaths")
#axs[1].plot(df['new_deaths_delayed'], label="Deaths (Delayed)")
axs[1].legend()

#for avg_days_from_symptoms_to_death in [14, 21, 28, 35]:
#    df['mortality_rate'] = df['new_deaths'] / df['new_cases'].shift(avg_days_from_symptoms_to_death)
#    axs[2].plot(df['mortality_rate'], label=f"Mortality Rate {avg_days_from_symptoms_to_death}d")
axs[2].plot(df['mortality_rate'], label=f"Mortality Rate {avg_days_from_symptoms_to_death}d")
axs[2].set_ylim(0, 0.05)
axs[2].legend()

plt.show()

