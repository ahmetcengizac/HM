from src.data.dboperator import db, ma
from src.util.funcs import slugify, now

#Mapping with database and Author, Article entities in this module

class Author( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 50 ), nullable=False )


class Article( db.Model ):
    _isupdate = 0
    id = db.Column( db.Integer, primary_key=True )
    title = db.Column( db.String( 50 ), nullable=False )
    body = db.Column( db.String( 200 ), nullable=False )
    site = db.Column( db.String( 200 ), nullable=False )
    slug = db.Column( db.String( 255 ), nullable=False )
    author_id = db.Column( db.Integer, db.ForeignKey( 'author.id' ) )
    author = db.relationship( 'Author', backref='rewards' )

    created = db.Column( db.DateTime )
    updated = db.Column( db.DateTime )

#Set values to "slug", "created" and "updated" fields
    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify( kwargs.get( 'title', '' ) )
        if not 'updated' in kwargs:
            kwargs['updated'] = now()
        if not 'created' in kwargs:
            kwargs['created'] = now()
        super().__init__( *args, **kwargs )

    @property
    def isupdate(self):
        return self._isupdate

#When the updating process, the "slug" and "updated" fileds are set with new values.
    @isupdate.setter
    def isupdate(self, v):
        self.slug = slugify( self.title )
        self.updated = now()
        self._isupdate = v


class ArticleSchema( ma.ModelSchema ):
    class Meta:
        model = Article


class AuthorSchema( ma.ModelSchema ):
    class Meta:
        model = Author
