#!/usr/bin/env python3
"""
Flask Web App with i18n Support

Initializes a Flask app with Flask-Babel for multilingual support.
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Application Configuration"""
    LANGUAGES = ["en", "fr"]  # Supported languages (English, French)
    BABEL_DEFAULT_LOCALE = "en"     # Default locale (English)
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone (Coordinated Universal Time)


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)  # Initialize Flask-Babel with the application


@app.route("/")
def index():
    """Index Page

    Renders the '0-index.html' template from the './templates' directory.
    """
    return render_template('./templates/1-index.html')


if __name__ == "__main__":
    # Run the Flask App in Debug Mode (optional, for development)
    app.run(debug=True)
