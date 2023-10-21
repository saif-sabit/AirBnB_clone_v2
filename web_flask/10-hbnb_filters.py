#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
@app.route('/hbnb_filters/<id>', strict_slashes=False)
def hbnb_filters(id=None):
    """returns states list"""
    if id is not None:
        id=id
    states = storage.all("State")
    return render_template('10-hbnb_filters.html', states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)