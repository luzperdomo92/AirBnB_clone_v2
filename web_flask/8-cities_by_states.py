#!/usr/bin/python3
"""  starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


# @app.route('/states_list', strict_slashes=False)
# def list_states():
#     states_list = storage.all(State).values()
#     return render_template('7-states_list.html', states_list=states_list)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states_list = storage.all(State).values()
    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def teardown_storage(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
