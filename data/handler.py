from util.static import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:first@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy( app )
ma = Marshmallow( app )


def insert(self):
    db.session.add( self )
    db.session.commit()

def update(self):
    db.session.add( self )
    db.session.commit()

def delete(self,**pid):
    rec = self.query.get(pid)
    db.session.delete(rec)
    db.session.commit()


