from flask import Flask
from flaskr.data import reset_total_urls_to
import flask_monitoringdashboard as dashboard


# app: single, global app instance
# name: module name, i.e. flaskr
app = Flask(__name__)
dashboard.bind(app)

# need this import for the routes to actually get added
from flaskr import routes

app.cli.add_command(reset_total_urls_to)
