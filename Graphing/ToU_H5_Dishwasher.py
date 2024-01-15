import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ukdale_h5_dishwasher_ToU_thirty.csv')

fig, ax = plt.subplots()

ax.hist(df['activity_start_rounded'], bins = 25, edgecolor = 'white')
plt.xticks(fontsize = 12)
xticks = ax.xaxis.get_major_ticks()
xticks[-1].label1.set_visible(False)
fig.autofmt_xdate(rotation=30, ha='center')
plt.yticks(fontsize=12)
plt.xlabel('Time of Use', fontsize=24)
plt.ylabel('Instances', fontsize=24)
plt.title('Time of Use for a Dishwasher in UKDALE House 5.', fontsize = 32)
plt.show()