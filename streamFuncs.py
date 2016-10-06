import httplib
import json
clientId = 'opposq941af1ooy9hwob1gud9ixogm0'

def getTwitchStreams():
  conn = httplib.HTTPSConnection('api.twitch.tv')
  conn.connect()
  request = conn.putrequest('GET', '/kraken/streams?game=StarCraft+II&client_id=' + clientId)
  conn.putheader('Content-Type','application/json')
  conn.endheaders()
  conn.send('')
  return json.loads(conn.getresponse().read())


def getTwitchChannels():
  return (k[u'channel'] for k in getTwitchStreams()[u'streams'])
