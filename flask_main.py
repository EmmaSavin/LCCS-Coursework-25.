#Click on blue link outputted on screen
#stop previous code. On the browser hold ctrl and click refresh to clear the cache

from flask import Flask, render_template #Added the render_template library

#Lets flask know this is the main program
app = Flask(__name__)

#The home page of the website is ('/').
@app.route('/')
def home():
    
    #define variables
    
    #pass these onto the webpage (with a chance to rename them)
    return render_template("index.html")

#@app.route("/



app.run(debug=False)