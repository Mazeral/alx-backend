#!/usr/bin/env python3

from flask import Flask, render_template

# In Python, __name__ is a built-in variable that holds the
# name of the current module. Its value depends on how the
# Python script is executed:
# When a script is run directly (e.g., python my_script.py):
# __name__ is set to the string "__main__".
# When a script is imported as a module in another script
# (e.g., import my_script):
# __name__ is set to the name of the module (e.g., "my_script").

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('./templates/0-index.html')


if __name__ == "__main__":
    # Run the Flask app in debug mode (optional, but helpful for development)
    app.run(debug=True)
