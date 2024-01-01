#!/usr/bin/python3
"""List states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(err):
    """tear down"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """List cities by states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    state_city = []
    for state in states:
        state_city.append([state, sorted(state.cities,
                                         key=lambda key: key.name)])
    return render_template('8-cities_by_states.html',
                           states=state_city)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
