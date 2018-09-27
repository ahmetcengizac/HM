import json
import requests

api_url = 'http://127.0.0.1:5000/insert'

data = {"title": "Heart of Midlothian",
        "body" : "this is large body area",
        "site" : "www.kt.com"
        }

data_json = json.dumps( data )
headers = {'Content-type': 'application/json'}

r = requests.post( url=api_url, auth=("userN", "passW"), data=data_json, headers=headers )

print( r.status_code, r.reason, r.text )
