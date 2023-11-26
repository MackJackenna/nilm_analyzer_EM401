import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ukdale_h5_dishwasher_DoU.csv')

plt.hist(df['duration_in_minutes'], bins = 30, edgecolor = 'white')
plt.xticks(np.arange(start=0, stop=130, step=5))
plt.xlabel('Minutes')
plt.ylabel('Instances')
plt.title('Duration of Use for a Dishwasher in UKDALE House 5.')
plt.show()