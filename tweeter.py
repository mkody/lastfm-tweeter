import pylast
from twitter import *
import time

###################PYLAST AUTH#############################################################

API_KEY = 			'YOUR LASTFM API KEY HERE'
API_SECRET = 			'YOUR LASTFM API SECRET KEY HERE'
username = 			'YOUR LASTFM USERNAME'
password_hash = pylast.md5(
				'YOUR LASTFM PASSWORD')

network = pylast.get_lastfm_network(
api_key = API_KEY, api_secret = API_SECRET,
username = username, password_hash = password_hash)
user = pylast.User(username, network)

###################PYLAST AUTH#############################################################

###################TWITTER AUTH############################################################

t = Twitter(
	auth=OAuth(
		'YOUR TWITTER TOKEN KEY', 
		'YOUR TWITTER TOKEN SECRET KEY',
		'YOUR TWITTER CONSUMER KEY',
		'YOUR TWITTER CONSUMER SECRET KEY')
)

###################TWITTER AUTH#############################################################


while True:
	with open("current.txt", "r+") as f:
		old = f.readline()
		current = str(user.get_now_playing())
		if old == current:
			pass
		else:
			if 'None' != current:
				f.seek(0)
				f.truncate()
				f.write(current)
				t.statuses.update(status="#NowPlaying " + current)
		f.close()
time.sleep(60)
