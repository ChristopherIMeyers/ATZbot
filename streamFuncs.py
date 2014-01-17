import httplib
import json

def getTwitchStreams():
	conn = httplib.HTTPSConnection('api.twitch.tv')
	conn.connect()
	request = conn.putrequest('GET', '/kraken/streams?game=StarCraft+II%3A+Heart+of+the+Swarm')
	conn.putheader('Content-Type','application/json')
	conn.endheaders()
	conn.send('')
	return json.loads(conn.getresponse().read())


def getTwitchChannels():
	return (k[u'channel'] for k in getTwitchStreams()[u'streams'])

def getStreamData(channelName):
	conn = httplib.HTTPSConnection('api.twitch.tv')
	conn.connect()
	request = conn.putrequest('GET', '/kraken/streams?channel='+channelName)
	conn.putheader('Content-Type','application/json')
	conn.endheaders()
	conn.send('')
	return json.loads(conn.getresponse().read())

def isStreamUp():
	return getStreamData('egjd')['streams'] != []
