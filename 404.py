# Importing Flask modules
from flask import Flask, render_template

# Initialize flask
app = Flask(__name__)


# Define the root URL and status code as 404
@app.route("/")
def page_not_found():
    return render_template('404.html'), 404


# Start the Flask web server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
