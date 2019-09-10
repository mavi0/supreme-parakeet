import base64
import json
import urllib2

# Authenticate Session
def auth(url, user, pwd):
    req = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (user, pwd)).replace('\n', '')
    req.add_header('Authorization', 'Basic %s' % base64string)
    return req

# Send JSON
def post_reroute(url, reroute_JSON):
    try:
        req = auth(url, "onos", "rocks")
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, data=reroute_JSON)
        return json.loads(response.read())
    except IOError as e:
        print(e)
        return

# Load JSON from file
def main():
    with open("reroute.json", 'r') as f:
        reroute_JSON = json.load(f)
        post_reroute('http://51.15.59.76:8181/onos/v1/imr/imr/reRouteIntents', json.dumps(reroute_JSON))

main()