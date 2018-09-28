This application is a RESTFULL microservice and works for the Article CRUD operations on the Posrtgress DB.
You can follow the steps below to try the application by creating the DB.

*To create a DB on Postgres
*To Change to DB connection string to SQLALCHEMY_DATABASE_URI parameter on src/data/dboperator.py
*To create DB elements (on python)
   >>>  from src.data.model import *
   >>>  db.create_all()

*You can use the test.py file to test. At the end of this file you can find the necessary functions for testing.

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

* Default service credential is {"UserName" : "userN", "Password" : "passW"}



Pre-requirements (pip install)
* Flask
* Flask-SQLAlchemy
* flask-marshmallow
* Pillow
