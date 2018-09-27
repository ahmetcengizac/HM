import json
import requests

api_url = 'http://127.0.0.1:5000/insert'
headers = {'Content-type': 'application/json'}


def test_insert():
    data = {"title": "Heart of Midlothian",
            "body": "this is large body area",
            "site": "www.kt.com",
            "author": 1
            }

    data_json = json.dumps( data )
    r = requests.post( url=api_url, auth=("userN", "passW"), data=data_json, headers=headers )

    print( r.status_code, r.reason, r.text )


test_insert()
