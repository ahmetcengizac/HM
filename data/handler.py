from util.static import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:first@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy( app )
ma = Marshmallow( app )


class DBHandler(db.Model):
    def insert(self):
        db.session.add( self )
        db.session.commit()

