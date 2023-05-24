#!/usr/bin/env python3
"""Script - > Basic Flask app module"""
from flask_babel import Babel
from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
from flask_caching import Cache
import os

class Config:
    """Flask Babel confgs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
app.wsgi_app = ProxyFix(app.wsgi_app)
babel = Babel(app)
cache = Cache(app)

@app.route('/')
@cache.cached()
def get_index() -> str:
    """method- > index page"""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
