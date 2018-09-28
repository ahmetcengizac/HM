import os

from flask import Flask

#To initialize Flask App

app = Flask(__name__)


IMAGE_ROOT = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'images')