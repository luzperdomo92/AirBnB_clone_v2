#!/usr/bin/python3
"""  starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    states_list = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states_list=states_list,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_storage(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
