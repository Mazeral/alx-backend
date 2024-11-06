#!/usr/bin/env python3

"""
Flask Web App with i18n Support.

Initializes a Flask app with Flask-Babel for multilingual support.
"""

from flask import (
    Flask, 
    render_template, 
    request
)
from flask_babel import (
    Babel, 
    localeselector
)
from typing import Dict
import requests


# User Data ( Mock )
users: Dict[int, Dict[str, str]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Application Configuration.

    Defines supported languages, default locale, and timezone.
    """
    LANGUAGES: list[str] = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE: str = "en"     # Default locale
    BABEL_DEFAULT_TIMEZONE: str = "UTC"  # Default timezone


app: Flask = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel: Babel = Babel(app)  # Initialize Flask-Babel with the application


@app.route("/")
def index() -> str:
    """
    Index Page.

    Renders the '1-index.html' template from the './templates' directory.
    """
    return render_template('./templates/1-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Locale Selector.

    Determines the best matching locale based on the user's accepted languages.
    """
    user_locale = request.accept_languages
    if user_locale in app.config['LANGUAGES']:
        return user_locale.best_match(app.config['LANGUAGES'])
    else:
        return app.config['BABEL_DEFAULT_LOCALE']


def get_user() -> int:
    """
    Retrieves the user ID from the request query string.

    Args:
        None

    Returns:
        int: The user ID (if found), otherwise None
    """
    login_as = request.args.get('login_as', type=int)
    return login_as


@app.before_request
def before_request() -> None:
    """
    Sets the global user variable before each request.

    Retrieves the user ID using `get_user()` and assigns it to `flask.g.user`.
    """
    flask.g.user = get_user()


if __name__ == "__main__":
    # Run the Flask App in Debug Mode (optional, for development)
    app.run(debug=True)
