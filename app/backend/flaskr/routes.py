# same single app instance 
from flaskr import app
from flask import render_template
import random


@app.route("/view")
def view():
    # Assumes index.html is in default templates folder, through this can be changed
    return render_template("index.html", action=random.randint(0, 100))
