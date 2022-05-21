#!/usr/bin/python3
"""
init file
"""

import api.v1.views.amenities
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from api.v1.views.index import *
import api.v1.views.states
import api.v1.views.cities
