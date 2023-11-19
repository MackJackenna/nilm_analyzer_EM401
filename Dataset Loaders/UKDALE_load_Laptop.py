from nilm_analyzer.loaders import UKDALE_Loader
import pandas as pd

from utilities import convert_timestamps2minutes
ukdale = UKDALE_Loader(data_path=r'C:\Users\44749\NILM\nilm_analyzer_EM401\UKDALE')

##Takes specific appliance data for whatever combination of houses
#a = ukdale.get_appliance_data(appliance="dishwasher", houses=[1])

##Takes whole dataset for individual house, including aggregate and all appliances
a = ukdale.get_house_data(house = 4)

b = convert_timestamps2minutes(pd.Series(a))
#c = a.data
#d = print(a.data)
print(b)

#df = pd.DataFrame(a,None,None)

#df.to_csv(r'E:\NILM\nilm_analyzer_EM401\Data.csv', index=True, header=True)