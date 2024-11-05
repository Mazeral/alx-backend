#!/usr/bin/env python3

"""
Flask Web App with i18n Support

Initializes a Flask app with Flask-Babel for multilingual support.
"""

from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import (
    Babel,
    babel
)


class Config:
    """
    Application Configuration

    Defines supported languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages (English, French)
    BABEL_DEFAULT_LOCALE = "en"     # Default locale (English)
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)  # Initialize Flask-Babel with the application


@app.route("/")
def index():
    """
    Index Page

    Renders the '1-index.html' template from the './templates' directory.
    """
    return render_template('./templates/1-index.html')


@babel.localeselector
def get_locale():
    """
    Locale Selector

    Determines the best matching locale based on the user's accepted languages.
    """
    accepted_languages = request.accept_languages
    best_match = accepted_languages.best_match(app.config['LANGUAGES'])
    return best_match or app.config['BABEL_DEFAULT_LOCALE']


if __name__ == "__main__":
    # Run the Flask App in Debug Mode (optional, for development)
    app.run(debug=True)
