# README.md

Internationalization (i18n) Project
=====================================

This project demonstrates the implementation of internationalization (i18n) in a Flask web application. The project consists of six tasks, each building upon the previous one to create a fully functional i18n-enabled application.

### Tasks

#### 0. Basic Flask App

* Create a basic Flask app with a single route and an index.html template.
* The template displays "Welcome to Holberton" as the page title and "Hello world" as the header.

#### 1. Basic Babel Setup

* Install the Babel Flask extension and instantiate the Babel object.
* Create a Config class to configure available languages and set the default locale and timezone.
* Use the Config class as the config for the Flask app.

#### 2. Get Locale from Request

* Create a get_locale function with the babel.localeselector decorator.
* Use request.accept_languages to determine the best match with supported languages.

#### 3. Parametrize Templates

* Use the _ or gettext function to parametrize templates.
* Create a babel.cfg file to configure Babel.
* Initialize translations and compile dictionaries.

#### 4. Force Locale with URL Parameter

* Modify the get_locale function to detect the locale argument in the URL parameter.
* If the locale is supported, return it; otherwise, resort to the previous default behavior.

#### 5. Mock Logging In

* Create a user table to mock a database user table.
* Define a get_user function to return a user dictionary or None if the ID cannot be found.
* Define a before_request function to set the user as a global on flask.g.user.
* Display a welcome message or a default message in the HTML template.

#### 6. Use User Locale

* Modify the get_locale function to use a user's preferred locale if it is supported.
* The order of priority is:
	1. Locale from URL parameters
	2. Locale from user settings
	3. Locale from request header
	4. Default locale

### Files and Directories

* `0-app.py`, `1-app.py`, `2-app.py`, `3-app.py`, `4-app.py`, `5-app.py`, `6-app.py`: Flask app files for each task.
* `templates/0-index.html`, `templates/1-index.html`, `templates/2-index.html`, `templates/3-index.html`, `templates/4-index.html`, `templates/5-index.html`, `templates/6-index.html`: HTML template files for each task.
* `babel.cfg`: Configuration file for Babel.
* `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`: Translation files for English and French.
* `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`: Compiled translation files for English and French.

### Author

Mohammad Omar Siddiq

### Directory

0x02-i18n
