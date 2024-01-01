#!/usr/bin/python3
"""List cities by states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(err):
    """tear down"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def the_states(id=None):
    """List states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda key: key.name)
    found = 0
    state = ""
    cities = []

    for stat in states:
        if id == stat.id:
            state = stat
            found = 1
            break
    if found:
        states = sorted(state.cities, key=lambda key: key.name)
        state = state.name

    if id and not found:
        found = 2

    return render_template("9-states.html", state=state,
                           array=states, found=found)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
