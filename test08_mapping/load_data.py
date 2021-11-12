import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns

# %%

cases = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
deaths = pd.read_csv("../../../Opensource/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")

# %%

df = cases
df = df.rename(columns={"Combined_Key": "County"})

# %%
import xml.etree.ElementTree as ET
tree = ET.parse('Usa_counties_large.svg')
root = tree.getroot()