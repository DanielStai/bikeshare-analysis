import pandas as pd
from datetime import datetime 

# Load the data. The files are available in the data folder in the google driv link provided in the README.

january_data = pd.read_csv('trip_data/january2021.csv')
feb_data = pd.read_csv('trip_data/feb2021.csv')
march_data = pd.read_csv('trip_data/march2021.csv')
april_data = pd.read_csv('trip_data/april2021.csv')
may_data = pd.read_csv('trip_data/may2021.csv')
june_data = pd.read_csv('trip_data/june2021.csv')
july_data = pd.read_csv('trip_data/july2021.csv')
august_data = pd.read_csv('trip_data/august2021.csv')
september_data = pd.read_csv('trip_data/september2021.csv')
october_data = pd.read_csv('trip_data/october2021.csv')
november_data = pd.read_csv('trip_data/november2021.csv')
december_data = pd.read_csv('trip_data/december2021.csv')

# Combine the data into one dataframe.

whole_year_data = pd.concat([january_data, feb_data, march_data, april_data, may_data, june_data, july_data, august_data, september_data, october_data, november_data, december_data])

# Drop the columns that are not needed.

modified_year_data = whole_year_data[['ride_id', 'rideable_type', 'start_station_id','start_station_name', 'end_station_id','end_station_name', 'started_at', 'ended_at', 'member_casual']]

#Check the data type of the columns and change the data types to the correct data type.

whole_year_data.dtypes
modified_year_data['started_at'] = pd.to_datetime(modified_year_data['started_at'])