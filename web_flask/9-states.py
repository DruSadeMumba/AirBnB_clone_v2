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
    states = get_states_by_id(id)
    return render_template('9-states.html', states=states, id=id)


def get_states_by_id(id):
    """get states by id"""
    states = storage.all(State)
    if id:
        key = f"{State.__name__}.{id}"
        states = states.get(key, None)
    else:
        states = states.values()
    return states


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
