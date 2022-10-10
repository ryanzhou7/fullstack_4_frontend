#!/bin/bash
# please run this with bash

cd ..

VENV=test_venv

# run venv as an module, 2nd venv passed as arugment (the name of the virtual env)
python3 -m venv $VENV

source $VENV/bin/activate

which python3

# assumes requirements.txt in folder
pip install
