import re
from datetime import datetime

from PIL import Image
from idna import unicode
from unidecode import unidecode

_punct_re = re.compile( r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+' )


# To create slug field.
def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split( text.lower() ):
        result.extend( unidecode( word ).split() )
    return unicode( delim.join( result ) )


# Get current time
def now():
    return datetime.now()

# Image crops functions

def crop_image1x1(filename, cropfile):
    original = Image.open( filename )
    original.show()

    width, height = original.size  # Get dimensions
    if height > width:
        left = 0
        right = width
        top = (height - width) // 2
        bottom = height - (height - width) // 2
    else:
        left = (width - height) // 2
        right = width - (width - height) // 2
        top = 0
        bottom = height
    c_image = original.crop( (left, top, right, bottom) )
    c_image.save( cropfile )


def crop_image2x1(filename, cropfile):
    original = Image.open( filename )
    original.show()

    width, height = original.size  # Get dimensions

    if height > width // 2:
        left = 0
        right = width
        top = (height-(width/2)) // 2
        bottom = height - (height-(width/2)) // 2
    else:
        left = (width - (height*2)) // 2
        right = width - (width - (height*2)) // 2
        top = 0
        bottom = height
    c_image = original.crop( (left, top, right, bottom) )
    c_image.save( cropfile )


def crop_image4x3(filename, cropfile):
    original = Image.open( filename )
    original.show()

    width, height = original.size  # Get dimensions

    if height // 3 > width // 4:
        left = 0
        right = width
        top = (height-(width/4*3)) // 2
        bottom = height - (height-(width/4*3)) // 2
    else:
        left = (width - (height/3*4)) // 2
        right = width - (width - (height/3*4)) // 2
        top = 0
        bottom = height
    c_image = original.crop( (left, top, right, bottom) )
    c_image.save( cropfile )


def crop_image16x9(filename, cropfile):
    original = Image.open( filename )
    original.show()

    width, height = original.size  # Get dimensions

    if height // 9 > width // 16:
        left = 0
        right = width
        top = (height-(width/16*9)) // 2
        bottom = height - (height-(width/16*9)) // 2
    else:
        left = (width - (height/9*16)) // 2
        right = width - (width - (height/9*16)) // 2
        top = 0
        bottom = height
    c_image = original.crop( (left, top, right, bottom) )
    c_image.save( cropfile )
