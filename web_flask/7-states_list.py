#!/usr/bin/python3
"""
Start a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    list states
    """
    template = '7-states_list.html'
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
