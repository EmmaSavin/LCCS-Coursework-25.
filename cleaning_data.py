import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set the file path
original_file_path = 'raw_data.csv'

# Read the file using a Python Data Analysis (pandas)
data = pd.read_csv(original_file_path)

#Remove special characters like *
data = data.replace({r'\*': ''}, regex=True)

#Save cleaned data to a new file
new_file = 'clean_data.csv'
data.to_csv(new_file, index=False)

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

##############Scatter Plot###############
fig = go.Figure(
    data=[
        go.Scatter(x=data.index, y=data['January_salinity'], mode='markers', name="January Salinity"),
        go.Scatter(x=data.index, y=data['June_salinity'], mode='markers', name="June Salinity"),
        go.Scatter(x=data.index, y=data['January_temp'], mode='markers', name="January Temperature"),
        go.Scatter(x=data.index, y=data['June_temp'], mode='markers', name="June Temperature"),
    ],
    layout=dict(
        title="Scatter Plot: Salinity and Temperature in January and June",
        yaxis_title="Temperature and Salinity",
        xaxis_title="Months (January and June)",
        xaxis=dict(showticklabels=False)
    ),
)

fig.show()


###############Bar Chart for temp##############

import plotly.express as px
import pandas as pd

df = pd.read_csv("clean_data.csv");

df_long = pd.melt(df, value_vars=["January_temp", "June_temp"],
                  var_name="month", value_name="temperature")


# Replace column names to make it more readable
df_long['month'] = df_long['month'].replace({"January_temp": "January", "June_temp": "June"})

df_long['months'] = df_long.index

fig = px.bar(df_long, x="months", y="temperature", color="month", barmode="group", height=400)
   
fig.update_layout(title = "Bar Chart: Temperatures in January and June")   
   
fig.show()

###############Bar Chart for salinity##############

import plotly.express as px
import pandas as pd

df = pd.read_csv("clean_data.csv");

df_long = pd.melt(df, value_vars=["January_salinity", "June_salinity"],
                  var_name="month", value_name="salinity")

# Replace column names to make it more readable
df_long['month'] = df_long['month'].replace({"January_salinity": "January", "June_salinity": "June"})

df_long['months'] = df_long.index

fig = px.bar(df_long, x="months", y="salinity", color="month", barmode="group", height=400)

fig.update_layout(title = "Bar Chart: Salinity Levels in January and June")

fig.show()
