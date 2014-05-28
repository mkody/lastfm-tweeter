import pylast
import twitter
import time

###################PYLAST AUTH#############################################################

API_KEY = 			''
API_SECRET = 		''
username = 			''
password_hash = pylast.md5(
					'')

network = pylast.get_lastfm_network(
api_key = API_KEY, api_secret = API_SECRET,
username = username, password_hash = password_hash)
user = pylast.User("", network)

###################PYLAST AUTH#############################################################

###################TWITTER AUTH############################################################

api = twitter.Api(
					consumer_key='',
					consumer_secret='',
					access_token_key='', 
					access_token_secret='')

###################TWITTER AUTH#############################################################


while True:
	with open("current.txt", "r+") as f:
		old = f.readline()
		current = str(user.get_now_playing())
		if old == current:
			pass
		else:
			f.seek(0)
			f.truncate()
			f.write(current)
			api.PostUpdate("Now Playing: " + current)
		f.close()
time.sleep(60)