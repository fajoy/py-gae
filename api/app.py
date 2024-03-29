# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello %s!' % app.config['SITENAME'].title()



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500



