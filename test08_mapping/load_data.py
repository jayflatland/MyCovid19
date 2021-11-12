import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
from county_to_county_code_map import county_to_county_code_map

# %%

cases = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
deaths = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")

# %%

df = cases
df = df.rename(columns={"Combined_Key": "County"})

county_ids = pd.DataFrame(county_to_county_code_map)
df = df[df.columns[:11]]
df.merge(county_ids, how='left', on='County')

# %%
# import xml.etree.ElementTree as ET
# tree = ET.parse('Usa_counties_large.svg')
# root = tree.getroot()


# for e in root:
#     print(e)

# #root.findall('.//path')
