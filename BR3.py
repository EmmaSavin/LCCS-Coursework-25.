app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",
                           scatter_plot_html=scatter_plot_html,
                           temp_barchart_html=temp_barchart_html,
                           salinity_barchart_html=salinity_barchart_html)