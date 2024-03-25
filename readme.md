# Final Year EME Project Repository
> This project seeks to investigate domestic appliance use and its effect on the low voltage GB distribution network by visualisng and transforming NILM datasets. The following repository hosts files to visuaise raw NILM data, to predict reactive power measurements and synthesise load profiles, and an autoencoder implementation to infer time and duration of use patterns of wet appliances.

## Original Repository
>This repository was forked from Mahnoor Shahid's *nilm_analyzer* which hosted a useful package to visualise and process the UK-DALE and REFIT datasets.  Found here: https://github.com/mahnoor-shahid/nilm_analyzer

## How to acces:


## Requried Downloads
>These NILM datasets and some large processed files are requried for use with the project:  
REFIT dataset - https://pureportal.strath.ac.uk/files/52873459/Processed_Data_CSV.7z  
UKDALE dataset - http://data.ukedc.rl.ac.uk/simplebrowse/edc/efficiency/residential/EnergyConsumption/Domestic/UK-DALE-2017/UK-DALE-FULL-disaggregated/ukdale.zip  
Processed data - https://strath-my.sharepoint.com/:u:/g/personal/jack_mckenna_2019_uni_strath_ac_uk/ERUB_ktltxxNqkB6vRT2uGIBTotu9LVKjbb9_YTnA35pMA?e=JK5N3R

## Dependencies
The following pyhton packages and versions are relevant to this project:
>- python==3.11.8
>- dask==2023.10.0  
>- jupyter_client==8.6.0  
>- jupyter_core==5.5.0  
>- matplotlib==3.8.2  
>- matplotlib-inline==0.1.6  
>- nilm-analyzer==1.0.11  
>- numpy==1.26.1  
>- pandas==2.1.1  
>- scikit-learn==1.3.2  
>- seaborn==0.13.0  
>- tensorflow==2.15.0  

## Dataset References
>REFIT [United Kingdom] <br />
Murray, D., Stankovic, L. & Stankovic, V. An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study. Sci Data 4, 160122 (2017). https://doi.org/10.1038/sdata.2016.122 <br />
UK-DALE [United Kingdom] <br />
Kelly, J., Knottenbelt, W. The UK-DALE dataset, domestic appliance-level electricity demand and whole-house demand from five UK homes. Sci Data 2, 150007 (2015). https://doi.org/10.1038/sdata.2015.7 <br />






