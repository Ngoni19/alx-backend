#!/usr/bin/env python3
"""Script-> Basic Flask app with internationalization support.
"""
from typing import Union, Dict
from flask import Flask, render_template, request, g
import pytz
from flask_babel import Babel


class Config:
    """Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """method: Retrieves a user based on a user id.
    """
    login_ID = request.args.get('login_as', '')
    if login_ID:
        return users.get(int(login_ID), None)
    return None


@app.before_request
def before_request() -> None:
    """method: run some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """method: Retrieves the locale for a web page.
    """
    loc = request.args.get('locale', '')
    if loc in app.config["LANGUAGES"]:
        return loc
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """method: Retrieves the timezone for a web page.
    """
    time_zone = request.args.get('timezone', '').strip()
    if not time_zone and g.user:
        time_zone = g.user['timezone']
    try:
        return pytz.time_zone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
