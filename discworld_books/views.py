from.import app

from flask import render_template, json, url_for

@app.route('/')
def index():
	return render_template ('index.html')

#def book_data():
#	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#	json_url = os.path.jpoin(SITE_ROOT, "static", "data.json")
#	data = json.load(open(json_url))
#
#	return book_data = (book_data[0]['title']



