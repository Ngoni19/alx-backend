#!/usr/bin/env python3
"""Script -> Basic Flask app with internationalization support"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Flask Babel configs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Method: retrieves the locale for a web page"""
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda z: (z if '=' in z else '{}='.format(z)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """method: index page"""
    return render_template('4-index.html')
