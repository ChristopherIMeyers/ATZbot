import httplib
import json
import praw
import re

import settings as settings

import streamFuncs

def formatLink(channel):
	encodedName = channel[u'display_name'].replace("-","&#45;")
	return "[{0}]({1})".format(encodedName,channel[u'url'])


def formatTwitchStreams(channels):
	return " | ".join(map(formatLink, channels)) + "\n"


replace = formatTwitchStreams(streamFuncs.getTwitchChannels())


r = praw.Reddit(user_agent='ATZ bot!  Pipe Twitch data to Reddit')
r.login(settings.reddituser, settings.redditpass)
subreddit = r.get_subreddit("AllThingsZerg")


description_current = r.get_settings(subreddit)['description']
newdescription = re.sub(r'&gt; ##Live Now!\n[^-]+','&gt; ##Live Now!\n'+replace+'\n',description_current)

newdescription = newdescription.replace("&gt;",">")

r.update_settings(subreddit, description=newdescription)
