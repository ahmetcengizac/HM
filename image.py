

from src.data.dboperator import db, ma, storage, StdImageField
from src.util.funcs import slugify, now


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
    image = db.Column(
        StdImageField(
            storage=storage,
            variations={
                'thumbnail': {"width": 100, "height": 100, "crop": True}
            }
        ), nullable=True
    )

    created = db.Column( db.DateTime )
    updated = db.Column( db.DateTime )

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

    @isupdate.setter
    def isupdate(self, v):
        self.slug = slugify( self.title )
        self.updated = now()
        self._isupdate = v


class ArticleSchema( ma.ModelSchema ):
    class Meta:
        model = Article