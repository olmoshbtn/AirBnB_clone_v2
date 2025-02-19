#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Site Index
    """
    return 'Hello HBNB!'


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    """
    HBTN page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C' followed by variable text
    """
    return ' '.join(['C', text.replace('_', ' ')])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
