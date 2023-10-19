#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ returns c text"""
    return f'c {text.replace("_"," ")}'

@app.route('/python/<text>', strict_slashes=False)
def pyhton_route(text = "is cool"):
    """ returns python text"""
    return f'Python  {text.replace("_"," ")}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
