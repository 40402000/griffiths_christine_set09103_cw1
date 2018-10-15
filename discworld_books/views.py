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



