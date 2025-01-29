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

# Run the app (this starts the server)
if __name__ == "__main__":
    app.run(debug=False)
