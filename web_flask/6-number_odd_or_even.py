#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    """
    Python is cool!
    """
    return ' '.join(['Python', text.replace('_', ' ')])


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Display 'n is a number', only if n is an integer
    """
    return '{} is a number'.format


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """
    Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_template(n):
    """
    Display a HTML page only if n is an integer, specifying n is even or odd
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
