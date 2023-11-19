from nilm_analyzer.loaders import REFIT_Loader
import pandas as pd
refit = REFIT_Loader(data_path=r'C:\Users\44749\NILM\nilm_analyzer_EM401\refit')

#a = refit.get_appliance_names(house=1)

#kettle = refit.get_appliance_data(appliance="Kettle", houses=[1,2,3])

#a = kettle.data

a = refit.get_house_data(house=12)

#kettle.data

#df = pd.DataFrame(kettle)

#df.to_csv(r'C:\Users\Jack\Desktop\test2.csv', index=True, header=True)

print(a)




