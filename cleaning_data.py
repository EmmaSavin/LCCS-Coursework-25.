
import statistics
import pandas as pd
#import matplotlib.pyplot as plt
import csv

# Set the file path
original_file_path = 'raw_data.csv'

# Read the file using a Python Data Analysis (pandas)
data = pd.read_csv(original_file_path)

#Remove special characters like *
data = data.replace({r'\*': ''}, regex=True)

#Save cleaned data to a new file
new_file = 'clean_data.csv'
data.to_csv(new_file, index=False)

print("Done! The the clean file is named:", new_file)

#Define non-numeric columns
non_numeric = ['Arabian Sea', 'corals present']

#Create dictionary
statistics_dictionary = {}

for col in data.columns:
    if col not in non_numeric:
        data_statistics = data[col]
        
        statistics_dictionary[col] = {
        
        
        
        }

##########################################################

print("File closed")
