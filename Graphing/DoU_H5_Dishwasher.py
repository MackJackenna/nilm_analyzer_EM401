import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ukdale_h5_dishwasher_DoU.csv')

plt.hist(df['duration_in_minutes'], bins = 20)
plt.xlabel('Minutes')
plt.ylabel('Instances')
plt.title('Duration of Use for a Dishwasher in UKDALE House 5.')
plt.show()