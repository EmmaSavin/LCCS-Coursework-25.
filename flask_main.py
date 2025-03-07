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