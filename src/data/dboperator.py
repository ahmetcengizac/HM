import sqlalchemy
from src.util.static import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:first@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy( app )
ma = Marshmallow( app )
DatabaseError = sqlalchemy.exc.IntegrityError


def insert(model):
    db.session.add( model )
    db.session.commit()
    return model.id


def update():
    db.session.commit()


def delete(model, pid):
    rec = get( model, pid )
    if rec is not None:
        db.session.delete( rec )
        db.session.commit()
        result = pid
    else:
        result=0
    return result


def get(model, pid):
    row = model.query.get( pid )
    return row
