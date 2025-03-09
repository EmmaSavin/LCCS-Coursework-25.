import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

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
scatter_plot_fig = go.Figure(
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

scatter_plot_fig.show()
scatter_plot_html = scatter_plot_fig.to_html(full_html=False, include_plotlyjs="cdn")

###############Bar Chart for temp##############

#import plotly.express as px
#import pandas as pd

df = pd.read_csv("clean_data.csv");

df_long_temp = pd.melt(df, value_vars=["January_temp", "June_temp"],
                  var_name="month", value_name="temperature")


# Replace column names to make it more readable
df_long_temp['month'] = df_long_temp['month'].replace({"January_temp": "January", "June_temp": "June"})
df_long_temp['months'] = df_long_temp.index

temp_barchart_fig = px.bar(df_long_temp, x="months", y="temperature", color="month", barmode="group", height=400)
temp_barchart_fig.update_layout(title = "Bar Chart: Temperatures in January and June")   
   
temp_barchart_fig.show()
temp_barchart_html = temp_barchart_fig.to_html(full_html=False, include_plotlyjs="cdn")
###############Bar Chart for salinity##############

#import plotly.express as px
#import pandas as pd

df = pd.read_csv("clean_data.csv");

df_long_salinity = pd.melt(df, value_vars=["January_salinity", "June_salinity"],
                  var_name="month", value_name="salinity")

# Replace column names to make it more readable
df_long_salinity['month'] = df_long_salinity['month'].replace({"January_salinity": "January", "June_salinity": "June"})
df_long_salinity['months'] = df_long_salinity.index

salinity_barchart_fig = px.bar(df_long_salinity, x="months", y="salinity", color="month", barmode="group", height=400)
salinity_barchart_fig.update_layout(title = "Bar Chart: Salinity Levels in January and June")

salinity_barchart_fig.show()
salinity_barchart_html = salinity_barchart_fig.to_html(full_html=False, include_plotlyjs="cdn")



################FLASK###################
#Click on blue link outputted on screen
#stop previous code. On the browser hold ctrl and click refresh to clear the cache

from flask import Flask, render_template #Added the render_template library

#Lets flask know this is the main program
app = Flask(__name__)

#The home page of the website is ('/').
@app.route('/')
def home():
    #define variables
    cwinfo = "The salinity and temperature of the Arabian sea in January versus June."
    
    #pass these onto the webpage (with a chance to rename them)
    return render_template("index.html", cwinfo=cwinfo)

#Route for second page
@app.route('/second-page')
def second_page():
    return render_template("second-page.html",
                           scatter_plot_html=scatter_plot_html,
                           temp_barchart_html=temp_barchart_html,
                           salinity_barchart_html=salinity_barchart_html)

#Route for third page
@app.route('/third-page')
def third_page():
    return render_template("third-page.html")

#Route for fourth page
@app.route('/fourth-page')
def fourth_page():
    return render_template("fourth-page.html")

#Route for fifth page
@app.route('/fifth-page')
def fifth_page():
    return render_template("fifth-page.html")

#Route for sixth page
@app.route('/sixth-page')
def sixth_page():
    return render_template("sixth-page.html")

#Route for seventh page
@app.route('/seventh-page')
def seventh_page():
    return render_template("seventh-page.html")


# Run the app (this starts the server)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5022, debug=False)
