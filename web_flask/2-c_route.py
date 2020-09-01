#!/usr/bin/python3
"""  starts a Flask web application """
from flask import Flask
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
