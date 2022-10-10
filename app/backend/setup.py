# https://github.com/amundsen-io/amundsen/blob/main/frontend/setup.py

import os
from setuptools import setup, find_packages

requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

__version__ = '1.0.0'

setup(
    name='flaskr',
    version=__version__,
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    dependency_links=[],
    install_requires=requirements,
    python_requires=">=3.6",
    options={"bdist_wheel": {"universal": True}},
)
# https://realpython.com/python-wheels/