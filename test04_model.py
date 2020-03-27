import os
import numpy as np
import pandas as pd
from pandas import Timestamp, Timedelta
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('jay1')


"""


N[t] - New cases on day t
T[t] - Total cases on day t
I - incubation period


E - average number of infectible people encountered while infectious per person


N[t] = T[t - I] * E[t]


"""