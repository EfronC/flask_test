import requests
import json
import time
import urllib

base_url = "https://api.diversitydata.io/"


def callDiversity(name):
	header = {'content-type':'application/json'}

	uri = {"fullname": name}

	uri = urllib.parse.urlencode(uri)

	url = base_url + "?" + uri

	r = requests.get(url, headers=header)
	res = json.loads(r.content)
	return res