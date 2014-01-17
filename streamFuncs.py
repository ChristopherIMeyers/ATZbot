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


def getTwitchChannels(jsonData):
	return (k[u'channel'] for k in jsonData[u'streams'])
