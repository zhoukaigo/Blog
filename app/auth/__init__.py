from flask import Blueprit

auth = Blueprit('auth', __name__)

from . import views