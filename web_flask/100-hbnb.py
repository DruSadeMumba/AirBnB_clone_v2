#!/usr/bin/python3
""" HBNB filters """
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(err):
    """ Tear down """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB filters """
    states = storage.all(State).values()
    states = sorted(states, key=lambda key: key.name)
    stat = []

    for state in states:
        stat.append([state, sorted(state.cities, key=lambda key: key.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda key: key.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda key: key.name)

    return render_template('100-hbnb.html', states=stat,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
