#!/usr/bin/python3
"""
Start Flask application
web application specifications:
    Listening on 0.0.0.0, port 5000
    Routes:
        /: display 'Hello HBNB!'
        /hbnb: display 'HBNB'
        /c/<text>: display c is value of text
        /python/(<text>): display “Python ”,
        followed by the value of the text
        /number/<n>: display “n is a number” only if n is an integer
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
    return f"Python {escape(text.replace('_',' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number_route(n):
    """
    returns n is a number
    if n is  number
    """
    return f"{escape(n)} is number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
