#!/usr/bin/python3
"""  starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBTN():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"


@app.route('/c/<text>')
def C(text):
    new_text = text.replace("_", " ")
    return "C %s" % new_text


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text="is cool"):
    new_text = text.replace("_", " ")
    return "Python %s" % new_text


@app.route('/number/<int:n>')
def n_number(n):
    return "%d is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if (n % 2) == 0:
        text = "even"
    else:
        text = "odd"
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
