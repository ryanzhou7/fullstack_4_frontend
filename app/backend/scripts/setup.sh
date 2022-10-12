#!/bin/bash
# please run this with bash

cd ..

VENV=venv
rm -rf $VENV

# run venv as an module, 2nd venv passed as arugment (the name of the virtual env)
python3 -m venv $VENV

# upgrade python
python3 -m pip install --upgrade pip

. $VENV/bin/activate

pip install .
