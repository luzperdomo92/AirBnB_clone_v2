#!/usr/bin/python3
"""  starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<states_id>', strict_slashes=False)
def states_ids(states_id=None):
    state_found = None
    states_list = storage.all(State).values()
    if states_id is not None:
        state_found = next((state for state in states_list
                           if state.id == states_id), None)

    return render_template('9-states.html', states_list=states_list,
                           state_found=state_found, states_id=states_id)


@app.teardown_appcontext
def teardown_storage(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
