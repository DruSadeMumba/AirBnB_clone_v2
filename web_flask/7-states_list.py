#!/usr/bin/python3
"""List states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """List states"""
    return render_template("7-states_list.html",
                           states=storage.all("State").values())


@app.teardown_appcontext
def teardown():
    """tear down"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
