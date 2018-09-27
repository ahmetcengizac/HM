from data.dboperator import db, ma
from util.funcs import slugify

class Author( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 50 ), nullable=False )


class Article( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.String( 50 ), nullable=False )
    body = db.Column( db.String( 200 ), nullable=False )
    site = db.Column( db.String( 200 ), nullable=False )
    slug = db.Column( db.String( 255 ), nullable=False )
    author_id = db.Column( db.Integer, db.ForeignKey( 'author.id' ) )
    author = db.relationship( 'Author', backref='rewards' )
    image = db.Column( db.LargeBinary, nullable=True )
    created = db.Column( db.DateTime )
    updated = db.Column( db.DateTime )

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify( kwargs.get( 'title', '' ) )
        super().__init__( *args, **kwargs )


class ArticleSchema( ma.ModelSchema ):
    class Meta:
        model = Article


class AuthorSchema( ma.ModelSchema ):
    class Meta:
        model = Author


