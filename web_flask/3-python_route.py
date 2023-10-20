#!/usr/bin/python3
"""
Start Flask application
web application specifications:
    Listening on 0.0.0.0, port 5000
    Routes:
        /: display 'Hello HBNB!'
        /hbnb: display 'HBNB'
        /c/<text>: display c is value of text
"""

from flask import Flask, escape
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ returns c text"""
    return f"C {escape(text.replace('_',' '))}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def pyhton_route(text="is cool"):
    """ returns python text"""
    return f'Python  {escape(text.replace("_"," "))}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
