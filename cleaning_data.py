
#################################################################
#import statistics
import pandas as pd
#import matplotlib.pyplot as plt
#import csv

# Set the file path
original_file_path = 'raw_data.csv'

# Read the file using Pandas(pd)
data = pd.read_csv(original_file_path)

#Remove special characters like *
data = data.replace({r'\*': ''}, regex=True)

#Save cleaned data to a new file
new_file = 'clean_data.csv'
data.to_csv(new_file, index=False)

#Change all data to numerical from strings
numeric_columns = ['salinity', 'January_temp', 'June_temp']
for col in numeric_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')
    
print("Done! The the clean file is named:", new_file)

#Define non-numeric columns
non_numeric = ['Arabian Sea', 'corals present']

#Create dictionary
statistics_dictionary = {}

for col in data.columns: #Checks each column
    if col not in non_numeric: #skips any column that has no numerical data
        data_stats = data[col] #column seleced is "data_stats"
        
        statistics_dictionary[col] = {
            'Mean': data_stats.mean(), #mean of col
            'Mode': data_stats.mode().iloc[0] if not data_stats.mode().empty else np.nan, #mode of col
            'Median': data_stats.median(), #median of col
            'Range': data_stats.max() - data_stats.min() #range of col
        }
#Changing statistics dictionary into Data Frame
stats_df = pd.DataFrame.from_dict(statistics_dictionary)
        
print(stats_df)

##########################################################
