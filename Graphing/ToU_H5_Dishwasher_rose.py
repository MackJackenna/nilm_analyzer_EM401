import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
import pycircular

df = pd.read_csv('ukdale_h5_dishwasher_ToU_thirty.csv')
df['activity_start_rounded']= pd.to_datetime(df['activity_start_rounded'])
dates = df.loc[df['Instance'], 'activity_start_rounded']

dates.groupby(dates.dt.hour).count().plot(kind="bar")

time_segment = 'hour'  # 'hour', 'dayweek', 'daymonth
freq_arr, times = pycircular.utils.freq_time(dates , time_segment=time_segment)
dates_mean = times.values.mean()
fig, ax1 = pycircular.plots.base_periodic_fig(freq_arr[:, 0], freq_arr[:, 1], time_segment=time_segment)
plt.title('Time of use of a Dishwasher in UK-DALE House 5, Rounded to an Hour.')
ax1.bar([dates_mean], [1], width=0.1, label='Arithmetical Mean Hour')
ax1.legend(bbox_to_anchor=(-0.3, 0.05), loc="upper left", borderaxespad=0)

plt.show()
