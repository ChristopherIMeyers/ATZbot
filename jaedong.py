import httplib
import json
import praw
import re

import settings as settings

import streamFuncs

def formatLink(streamUp):
	if streamUp:
		statusString = "online!"
	else:
		statusString = "offline"
	return "[Jaedong's stream is **{0}**]({1})".format(statusString,'http://www.twitch.tv/EGJD')


streamStatus = formatLink(streamFuncs.isStreamUp())


r = praw.Reddit(user_agent='Jaedong bot!  Get current status of Jaedong\'s stream')
r.login(settings.reddituser, settings.redditpass)
subreddit = r.get_subreddit("Jaedong")


description_current = r.get_settings(subreddit)['description']
newdescription = re.sub(r'######[^\n]+','######'+streamStatus,description_current)

newdescription = newdescription.replace("&gt;",">")

r.update_settings(subreddit, description=newdescription)
