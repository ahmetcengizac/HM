import re
from datetime import datetime

from idna import unicode
from unidecode import unidecode

_punct_re = re.compile( r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+' )


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split( text.lower() ):
        result.extend( unidecode( word ).split() )
    return unicode( delim.join( result ) )

def now():
    return datetime.now()