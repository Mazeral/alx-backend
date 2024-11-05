#!/usr/bin/env python3

"""
Flask Web Application

This script initializes a basic Flask web application, serving an HTML template
from the './templates' directory.
"""

from flask import Flask, render_template

"""
**Built-in Variable: `__name__`**

In Python, `__name__` is a built-in variable that holds the name of the
current module. Its value depends on how the Python script is executed:

* **Direct Execution** (e.g., `python my_script.py`): `__name__` is set to
`"__main__"`.

* **Module Import** (e.g., `import my_script`): `__name__` is set to the
module name (e.g., `"my_script"`).
"""

# Initialize the Flask Application
app = Flask(__name__)

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
**Main Execution Block**

Check if this script is being executed directly (not imported as a module).
If so, run the Flask application in debug mode.
"""
if __name__ == "__main__":
    # Run the Flask App in Debug Mode (optional, but helpful for development)
    app.run(debug=True)
