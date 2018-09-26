from config import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:first@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy( app )
ma = Marshmallow( app )


class Author( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 50 ), nullable=False )


class Product( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.String( 50 ), nullable=False )
    body = db.Column( db.String( 200 ), nullable=False )
    author_id = db.Column( db.Integer, db.ForeignKey( 'author.id' ) )
    author = db.relationship( 'Author', backref='rewards' )


class ProductSchema( ma.ModelSchema ):
    class Meta:
        model = Product


class AuthorSchema( ma.ModelSchema ):
    class Meta:
        model = Author