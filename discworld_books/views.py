from.import app

from flask import render_template, json, url_for
from pprint import pprint
import os

@app.route('/')
def index():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('index.html', data=data)


@app.route('/chronologically')
def chronologically():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
		data = json.load (f)
                return render_template ('chronologically.html', data=data)

@app.route('/the_city_watch')
def the_city_watch():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                return render_template ('the_city_watch.html', data=data)

@app.route('/the_witches')
def the_witches():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                return render_template ('the_witches.html', data=data)

@app.route('/death')
def death():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                return render_template ('death.html', data=data)

@app.route('/moist_von_lipwig')
def moist_von_lipwig():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                return render_template ('moist_von_lipwig.html', data=data)


@app.route('/rincewind_the_wizards')
def rincewind_the_wizards():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                return render_template ('rincewind_the_wizards.html', data=data)

@app.route('/for_younger_readers')
def for_younger_readers():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                return render_template ('for_younger_readers.html', data=data)

