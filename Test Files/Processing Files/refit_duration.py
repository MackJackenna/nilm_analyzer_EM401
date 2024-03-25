#Just a python version of the jupyter notebook from the nilm_anlayzer for easier creation of the activations csvs

from nilm_analyzer.loaders import REFIT_Loader
import csv

i = 21

refit_data = REFIT_Loader(data_path=r'C:\Users\44749\NILM\nilm_analyzer_EM401\refit')
appliance_data = refit_data.get_appliance_data(appliance='dishwasher', houses=[i])
appliance_data.resample(sampling_period= 8)
appliance_data.data
appliance_data.get_activations(threshold_x=10.0, threshold_y=0.025)
a = appliance_data.activations[i].sort_values(by='duration_in_minutes', ascending=True)
a.to_csv(rf'C:\Users\44749\NILM\nilm_analyzer_EM401\Processed Data\DW Activations Useable\Activations\R_h{i}_activations.csv')