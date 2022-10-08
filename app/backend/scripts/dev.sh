#!/bin/bash

source ../venv/bin/activate

cd ..

# assumes starter file is named app.py / wsgi.py and in current directoy
# otherwise $ flask --app <file_name.py> run
# hot reload enabled
flask --debug run
# alternatively export FLASK_APP=<file_name.py> && flask run

# makes app available on same network
# flask --debug run --host=0.0.0.0