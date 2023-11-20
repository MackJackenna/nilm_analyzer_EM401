import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ukdale_h5_dishwasher_DoU_test.csv')

fig, ax = plt.subplots()

ax.hist(df['activity_start_rounded'], bins = 40)
fig.autofmt_xdate()
plt.xlabel('Time of Use')
plt.ylabel('Instances')
plt.title('Time of Use for a Dishwasher in UKDALE House 5.')
plt.show()