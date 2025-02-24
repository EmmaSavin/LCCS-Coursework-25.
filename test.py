import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set the file path
original_file_path = 'raw_data.csv'

try:
    # Read the file using pandas
    data = pd.read_csv(original_file_path)
except FileNotFoundError:
    print(f"Error: File '{original_file_path}' not found.")
    exit()

# Remove special characters like *
data = data.replace({r'\*': ''}, regex=True)

# Convert specific columns to numeric
numeric_columns = ['January_salinity', 'June_salinity', 'January_temp', 'June_temp']

for col in numeric_columns:
    if col in data.columns:
        # Convert column to numeric
        data[col] = pd.to_numeric(data[col], errors='coerce')
    else:
        print(f"Warning: Column '{col}' not found in the dataset.")

# Print the cleaned data before dropping NaNs
print("Cleaned Data (before dropping NaNs):")
print(data)

# Drop rows with NaN values but preserve the original file if needed
cleaned_data = data.dropna()

# Check if the cleaned DataFrame is empty
if cleaned_data.empty:
    print("Error: The DataFrame is empty after cleaning and preprocessing.")
    exit()

# Save the cleaned data to a new file
new_file = 'clean_data.csv'
cleaned_data.to_csv(new_file, index=False)

# Print the cleaned data to confirm
print("Cleaned Data (after dropping NaNs):")
print(cleaned_data)

# Statistics calculation
statistics_dictionary = {}

for col in numeric_columns:
    if col in cleaned_data.columns:
        data_stats = cleaned_data[col]
        statistics_dictionary[col] = {
            'Mean': data_stats.mean(),
            'Mode': data_stats.mode().iloc[0] if not data_stats.mode().empty else np.nan,
            'Median': data_stats.median(),
            'Range': data_stats.max() - data_stats.min(),
        }

# Convert statistics dictionary to a DataFrame for display
stats_df = pd.DataFrame.from_dict(statistics_dictionary, orient='index')

print("\nStatistics Summary:")
print(stats_df)

# Graphing using Plotly
fig = go.Figure(
    data=[
        go.Bar(x=cleaned_data.index, y=cleaned_data['January_salinity'], name="January Salinity"),
        go.Bar(x=cleaned_data.index, y=cleaned_data['June_salinity'], name="June Salinity"),
        go.Bar(x=cleaned_data.index, y=cleaned_data['January_temp'], name="January Temperature"),
        go.Bar(x=cleaned_data.index, y=cleaned_data['June_temp'], name="June Temperature"),
    ],
    layout=dict(
        title="Salinity and Temperature in January and June",
        barmode='group',
        bargap=0.3,
        bargroupgap=0.1,
    ),
)

fig.show()

print("Done! The cleaned file is saved as:", new_file)

##############################################################

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
#Changing statistics dictionary into Data Frame to display data in orderly format
stats_df = pd.DataFrame.from_dict(statistics_dictionary)
        
print(stats_df)





import plotly.graph_objects as go
import pandas as pd

df = data.dropna()

fig = go.Figure(
    data=[
        go.Bar(x=df.January_salinity, name="June Salinity"),
        go.Bar(x=df.June_salinity, name="June Salinity"),
        go.Bar(x=df.January_temp, name="January Temperature"),
        go.Bar(x=df.June_temp, name="June Temperature")
    ],
    layout=dict(
        title="Salinity and Temperature of Arabian Sea in January vs. June",
        barmode='group',
        bargap=0.3,
        bargroupgap=0.1,
    ),
)






















#################################################

import pandas as pd

# Set the file path
original_file_path = 'raw_data.csv'

# Read the file using a Python Data Analysis (pandas)
data = pd.read_csv(original_file_path)

#Remove special characters like *
data = data.replace({r'\*': ''}, regex=True)

#Save cleaned data to a new file
new_file = 'clean_data.csv'

#Change all data to numerical from strings
numeric_columns = ['January_salinity', 'June_salinity', 'January_temp', 'June_temp']
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
#Changing statistics dictionary into Data Frame to display data in orderly format
stats_df = pd.DataFrame.from_dict(statistics_dictionary)
        
print(stats_df)


#########################################################################

import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set the file path
original_file_path = 'raw_data.csv'

try:
    # Read the file using pandas
    data = pd.read_csv(original_file_path)
except FileNotFoundError:
    print(f"Error: File '{original_file_path}' not found.")
    exit()

# Remove special characters like *
data = data.replace({r'\*': ''}, regex=True)

# Convert specific columns to numeric
numeric_columns = ['January_salinity', 'June_salinity', 'January_temp', 'June_temp']

for col in numeric_columns:
    if col in data.columns:
        # Convert column to numeric
        data[col] = pd.to_numeric(data[col], errors='coerce')
    else:
        print(f"Warning: Column '{col}' not found in the dataset.")

# Print the cleaned data before dropping NaNs
print("Cleaned Data (before dropping NaNs):")
print(data)

# Drop rows with NaN values but preserve the original file if needed
cleaned_data = data.dropna()

# Check if the cleaned DataFrame is empty
if cleaned_data.empty:
    print("Error: The DataFrame is empty after cleaning and preprocessing.")
    exit()

# Save the cleaned data to a new file
new_file = 'clean_data.csv'
cleaned_data.to_csv(new_file, index=False)

# Print the cleaned data to confirm
print("Cleaned Data (after dropping NaNs):")
print(cleaned_data)

# Statistics calculation
statistics_dictionary = {}

for col in numeric_columns:
    if col in cleaned_data.columns:
        data_stats = cleaned_data[col]
        statistics_dictionary[col] = {
            'Mean': data_stats.mean(),
            'Mode': data_stats.mode().iloc[0] if not data_stats.mode().empty else np.nan,
            'Median': data_stats.median(),
            'Range': data_stats.max() - data_stats.min(),
        }

# Convert statistics dictionary to a DataFrame for display
stats_df = pd.DataFrame.from_dict(statistics_dictionary, orient='index')

print("\nStatistics Summary:")
print(stats_df)

# Graphing using Plotly
fig = go.Figure(
    data=[
        go.Bar(x=cleaned_data.index, y=cleaned_data['January_salinity'], name="January Salinity"),
        go.Bar(x=cleaned_data.index, y=cleaned_data['June_salinity'], name="June Salinity"),
        go.Bar(x=cleaned_data.index, y=cleaned_data['January_temp'], name="January Temperature"),
        go.Bar(x=cleaned_data.index, y=cleaned_data['June_temp'], name="June Temperature"),
    ],
    layout=dict(
        title="Salinity and Temperature in January and June",
        barmode='group',
        bargap=0.3,
        bargroupgap=0.1,
    ),
)

fig.show()

print("Done! The cleaned file is saved as:", new_file)
