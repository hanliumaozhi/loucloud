#!/usr/bin/env python
# encoding: utf-8

from .host import host
from .flask_app import app
from .dbs import db


app.register_blueprint(host)
