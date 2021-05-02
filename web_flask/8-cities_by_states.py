#!/usr/bin/python3
"""
Start a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    list cities by state
    """
    template = '8-cities_by_states.html'
    states = storage.all(State).values()
    return render_template(template, states=states)


@app.teardown_appcontext
def close_storage(exc):
    """
    close storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
