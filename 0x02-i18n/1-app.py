#!/usr/bin/env python3

"""
Flask Web Application with Internationalization (i18n) Support

This script initializes a Flask web application with Flask-Babel
for multilingual support.
"""

from flask import Flask, render_template
from flask_babel import Babel, Config

"""
**Application Initialization**

Create a new Flask application instance.
"""
app = Flask(__name__)

"""
**Flask-Babel Configuration**

Configure Flask-Babel for internationalization (i18n) support.
"""
babel_config = Config()

"""
**Supported Languages and Localization Settings**

Define the supported languages, default locale, and timezone.
"""
# List of supported languages (English, French)
babel_config.LANGUAGES = ["en", "fr"]
# Default locale (English)
babel_config.DEFAULT_LOCALE = "en"
# Default timezone (Coordinated Universal Time)
babel_config.DEFAULT_TIMEZONE = "UTC"

"""
**Route: Root (/)**

Define a route for the root URL ("/") of the application.
"""


@app.route("/")
def index():
    """
    **Index Page**

    Render the '0-index.html' template from the './templates' directory.
    """
    return render_template('./templates/0-index.html')


"""
**Initialize Flask-Babel with the Application**

Bind the Flask-Babel instance to the Flask application.
"""
# Pass the config to the Babel instance
babel = Babel(app, config=babel_config)

"""
**Main Execution Block**

Check if this script is being executed directly (not imported as a module).
If so, run the Flask application in debug mode.
"""
if __name__ == "__main__":
    # Run the Flask App in Debug Mode (optional, but helpful for development)
    app.run(debug=True)
