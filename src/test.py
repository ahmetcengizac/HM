import json
import requests

headers = {'Content-type': 'application/json'}
credentail = ("userN", "passW")

def test_create_author():
    data = {"name": "Hearts"
            }

    api_url = 'http://127.0.0.1:5000/create_author'
    data_json = json.dumps( data )
    r = requests.post( url=api_url, auth=credentail, data=data_json, headers=headers )

    print( r.status_code, r.reason, r.text )

def test_create():
    data = {"title": "Heart of Midlothian",
            "body": "this is large body area",
            "site": "www.kts.com",
            "author": "1"
            }

    api_url = 'http://127.0.0.1:5000/create'
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
    r = requests.post( url=api_url, auth=credentail )

    print( r.status_code, r.reason, r.text )


def test_read():
    api_url = 'http://127.0.0.1:5000/5'
    r = requests.get( url=api_url, auth=credentail )

    print( r.status_code, r.reason, r.text )


def test_upload():
    files = {'image': ('inputFile', open( 'C:\\Users\\ahmetc\\Pictures\\cde.jpg', 'rb' ))}

    api_url = 'http://127.0.0.1:5000/upload/1'
    r = requests.post( url=api_url, auth=credentail, files=files )

    print( r.status_code, r.reason, r.text )


def test_download():
    api_url = 'http://127.0.0.1:5000/download/1'
    r = requests.get( url=api_url, auth=credentail ,allow_redirects=True)
    open( '1.jpg', 'wb' ).write( r.content )


def test_download_crop():
    api_url = 'http://127.0.0.1:5000/download/3/16x9'
    r = requests.get( url=api_url, auth=credentail ,allow_redirects=True)
    open( '3_1.jpg', 'wb' ).write( r.content )


#####  for Author
# test_create_author()

##### for Article
#test_create()
#test_read()
#test_update()
#test_delete()

#test_upload()
#test_download()
#test_download_crop()