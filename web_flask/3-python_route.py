#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display message: Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display message: HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display message: C <text>"""
    msg = text.replace('_', ' ')
    return f"C {msg}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text='is cool'):
    """Display message: C <text>"""
    msg = text.replace('_', ' ')
    return f"Python {msg}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
