import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ukdale_h5_dishwasher_ToU_thirty.csv')

fig, ax = plt.subplots()

ax.hist(df['activity_start_rounded'], bins = 25, edgecolor = 'white')
plt.xticks(fontsize = 7)
xticks = ax.xaxis.get_major_ticks()
xticks[-1].label1.set_visible(False)
fig.autofmt_xdate(rotation=30, ha='left')
plt.xlabel('Time of Use')
plt.ylabel('Instances')
plt.title('Time of Use for a Dishwasher in UKDALE House 5.')
plt.show()