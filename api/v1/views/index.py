#!/usr/bin/python3
''' comment '''

from flask import jsonify
import index
from api.v1.views import app_views

@app_views.route('/status')
def get_status():
    ''' route status test that return a JSON query '''
    dict = {'status': 'OK'}
    return jsonify(dict)
