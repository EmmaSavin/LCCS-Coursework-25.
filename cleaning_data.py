

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

filename = 'clean_data.csv'

csvfile = open('clean_data.csv', "r")
df = pd.pandas.read_csv('clean_data.csv')
print("File Opened")
with open('clean_data.csv', 'r') as filename:
    csv_reader = pd.pandas.read_csv('clean_data.csv')
    for column in csv_reader:
        print(column[0], column[1], column[2], column[3], column[4])
        
csvfile.close()
print("File closed")
