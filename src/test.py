import json
import requests

headers = {'Content-type': 'application/json'}
credentail = ("userN", "passW")

def test_insert():
    data = {"title": "Heart of Midlothian 213123",
            "body": "this is large body area 12312",
            "site": "www.kt.com",
            "author": 2
            }

    api_url = 'http://127.0.0.1:5000/insert'
    data_json = json.dumps( data )
    r = requests.post( url=api_url, auth=credentail, data=data_json, headers=headers )

    print( r.status_code, r.reason, r.text )


def test_update():
    data = {"title": "Heart of Middlecity",
            "body": "this is middle body",
            "site": "www.ct.com",
            "author": 2
            }

    api_url = 'http://127.0.0.1:5000/update/10'
    data_json = json.dumps( data )
    r = requests.put( url=api_url, auth=credentail, data=data_json, headers=headers )

    print( r.status_code, r.reason, r.text )

def test_delete():
    api_url = 'http://127.0.0.1:5000/delete/26'
    r = requests.post( url=api_url, auth=credentail)

    print( r.status_code, r.reason, r.text )

def test_get():
    api_url = 'http://127.0.0.1:5000/5'
    r = requests.get( url=api_url, auth=credentail)

    print( r.status_code, r.reason, r.text )

test_update()
