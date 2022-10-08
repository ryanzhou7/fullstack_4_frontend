from flask import Flask

# app: single, global app instance
# name: module name, i.e. flaskr
app = Flask(__name__)

# need this import for the routes to actually get added
from flaskr import routes
