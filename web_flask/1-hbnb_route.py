#!/usr/bin/python3
"""
Start Flask application
web application specifications:
    Listening on 0.0.0.0, port 5000
    Routes:
        /: display 'Hello HBNB!'
        /hbnb: display 'HBNB'
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route display "HBNB"
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
