#!/usr/bin/env python3

from flask import Flask, render_template
from flask-babel import Babel
from flask-babel import Config


app = Flask(__name__)
babel_config = Config()

babel_config.LANGUAGES = ["en", "fr"]
babel_config.DEFAULT_LOCALE = "en"
babel_config.DEFAULT_TIMEZONE = "UTC"


@app.route("/")
def index():
    return render_template('./templates/0-index.html')


babel = Babel(app)

if __name__ == "__main__":
    # Run the Flask app in debug mode (optional, but helpful for development)
    app.run(debug=True)
