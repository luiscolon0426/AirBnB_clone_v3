#!/usr/bin/python3
''' this is just a __init__ method '''

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/vi')
