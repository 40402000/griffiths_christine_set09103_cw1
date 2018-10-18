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
@app.route('/the_colour_of_magic')
def the_colour_of_magic():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[0]
                return render_template ('books.html', book_data=book_data)


@app.route('/the_light_fantastic')
def the_light_fantastic():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[1]
                return render_template ('books.html', book_data=book_data)

@app.route('/equal_rites')
def equal_rites():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[2]
                return render_template ('books.html', book_data=book_data)

@app.route('/mort')
def mort():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[3]
                return render_template ('books.html', book_data=book_data)

@app.route('/sourcery')
def sourcery():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[4]
                return render_template ('books.html', book_data=book_data)

@app.route('/wyrd_sisters')
def wyrd_sisters():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[5]
                return render_template ('books.html', book_data=book_data)

@app.route('/pyramids')
def pyramids():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[6]
                return render_template ('books.html', book_data=book_data)

@app.route('/guards_guards')
def guards_guards():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[7]
                return render_template ('books.html', book_data=book_data)

@app.route('/faust_eric')
def faust_eric():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[8]
                return render_template ('books.html', book_data=book_data)

@app.route('/moving_pictures')
def moving_pictures():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[9]
                return render_template ('books.html', book_data=book_data)

@app.route('/reaper_man')
def reaper_man():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[10]
                return render_template ('books.html', book_data=book_data)

@app.route('/witches_abroad')
def witches_abroad():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[11]
                return render_template ('books.html', book_data=book_data)

@app.route('/small_gods')
def small_gods():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[12]
                return render_template ('books.html', book_data=book_data)

@app.route('/lords_and_ladies')
def lords_and_ladies():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[13]
                return render_template ('books.html', book_data=book_data)

@app.route('/men_at_arms')
def men_at_arms():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[14]
                return render_template ('books.html', book_data=book_data)

@app.route('/soul_music')
def soul_music():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[15]
                return render_template ('books.html', book_data=book_data)

@app.route('/interesting_times')
def interesting_times():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[16]
                return render_template ('books.html', book_data=book_data)

@app.route('/maskerade')
def maskerade():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[17]
                return render_template ('books.html', book_data=book_data)

@app.route('/feet_of_clay')
def feet_of_clay():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[18]
                return render_template ('books.html', book_data=book_data)

@app.route('/hogfather')
def hogfather():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[19]
                return render_template ('books.html', book_data=book_data)

@app.route('/jingo')
def jingo():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[20]
                return render_template ('books.html', book_data=book_data)

@app.route('/the_last_continent')
def the_last_continent():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[21]
                return render_template ('books.html', book_data=book_data)


@app.route('/carpe_jugulum')
def carpe_jugulum():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[22]
                return render_template ('books.html', book_data=book_data)


@app.route('/the_fith_elephant')
def the_fith_elephant():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[23]
                return render_template ('books.html', book_data=book_data)


@app.route('/the_truth')
def the_truth():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[24]
                return render_template ('books.html', book_data=book_data)


@app.route('/theif_of_time')
def theif_of_time():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[25]
                return render_template ('books.html', book_data=book_data)


@app.route('/the_last_hero')
def the_last_hero():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[26]
                return render_template ('books.html', book_data=book_data)

@app.route('/the_amazing_maurice_and_his_educated_rodents')
def the_amazing_maurice_and_his_educated_rodents():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[27]
                return render_template ('books.html', book_data=book_data)


@app.route('/night_watch')
def night_watch():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[28]
                return render_template ('books.html', book_data=book_data)

@app.route('/the_wee_free_men')
def the_wee_free_men():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[29]
                return render_template ('books.html', book_data=book_data)

@app.route('/monstrous_regiment')
def monstrous_regiment():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[30]
                return render_template ('books.html', book_data=book_data)

@app.route('/a_hat_full_of_sky')
def a_hat_full_of_sky():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[31]
                return render_template ('books.html', book_data=book_data)

@app.route('/going_postal')
def going_postal():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[32]
                return render_template ('books.html', book_data=book_data)

@app.route('/thud')
def thud():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[33]
                return render_template ('books.html', book_data=book_data)

@app.route('/wintersmith')
def wintersmith():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[34]
                return render_template ('books.html', book_data=book_data)

@app.route('/making_money')
def making_money():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[35]
                return render_template ('books.html', book_data=book_data)

@app.route('/unseen_academicals')
def unseen_academicals():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[36]
                return render_template ('books.html', book_data=book_data)

@app.route('/i_shall_wear_midnight')
def i_shall_wear_midnight():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[37]
                return render_template ('books.html', book_data=book_data)

@app.route('/snuff')
def snuff():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[38]
                return render_template ('books.html', book_data=book_data)

@app.route('/raising_steam')
def raising_steam():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[39]
                return render_template ('books.html', book_data=book_data)

@app.route('/the_shepherds_crown')
def the_shepherds_crown():
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
                data = json.load (f)
                book_data=data[40]
                return render_template ('books.html', book_data=book_data)





