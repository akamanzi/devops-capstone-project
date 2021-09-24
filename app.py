"""
  Main flask app module. Define routes and app configurations
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    """
    route to the home page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    