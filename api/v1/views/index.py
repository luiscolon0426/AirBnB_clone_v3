#!/usr/bin/python3
''' module that have the get status '''

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route('/status')
def get_status():
    ''' route status test that return a JSON query '''
    dict = {'status': 'OK'}
    return jsonify(dict)


@app_views.route('/stats')
def newcount():
    data = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "place": storage.count(Place),
        "user": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(data)
