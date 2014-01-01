import httplib
import json
import praw
import re

import settings as settings

def getTwitchStreams():
	conn = httplib.HTTPSConnection('api.twitch.tv')
	conn.connect()
	request = conn.putrequest('GET', '/kraken/streams?game=StarCraft+II%3A+Heart+of+the+Swarm')
	conn.putheader('Content-Type','application/json')
	conn.endheaders()
	conn.send('')
	return json.loads(conn.getresponse().read())


def getTwitchChannels(jsonData):
	return (k[u'channel'] for k in jsonData[u'streams'])


def formatLink(channel):
	return "[{0}]({1})".format(channel[u'display_name'],channel[u'url'])


def formatTwitchStreams(channels):
	return " | ".join(map(formatLink, channels)) + "\n"


replace = formatTwitchStreams(getTwitchChannels(getTwitchStreams()))


r = praw.Reddit(user_agent='ATZ bot!  Pipe Twitch data to Reddit')
r.login(settings.reddituser, settings.redditpass)
subreddit = r.get_subreddit("AllThingsZerg")


description_current = r.get_settings(subreddit)['description']
newdescription = re.sub(r'&gt; ##Live Now!\n[^-]+','&gt; ##Live Now!\n'+replace+'\n',description_current)

newdescription = newdescription.replace("&gt;",">")

r.update_settings(subreddit, description=newdescription)
