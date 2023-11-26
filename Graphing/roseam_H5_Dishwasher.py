import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from windrose import WindroseAxes

df = pd.read_csv('ukdale_h5_dishwasher_rose_am.csv')

ax = WindroseAxes.from_ax()
ax.bar(df['direction'], df['activity_start_rounded'], normed = True, opening = 0.8, edgecolor='white')
ax.set_legend()

plt.title('Rose Diagram for a Dishwasher in UKDALE House 5.')
plt.show()