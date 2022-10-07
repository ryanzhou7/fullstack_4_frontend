#!/bin/bash
# please run this with bash

cd ..

# run venv as an module, 2nd venv passed as arugment (the name of the virtual env)
python3 -m venv venv

source venv/bin/activate

which python3

# assumes requirements.txt executing folder
pip install
