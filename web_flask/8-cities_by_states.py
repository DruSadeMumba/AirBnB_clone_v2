#!/usr/bin/python3
"""List cities by states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """tear down"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """List cities"""
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
