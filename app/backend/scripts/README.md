- flask app was able to run with only flaskr installed?
- on local computer
`python3 -m venv venv`
`source venv/bin/activate`

```python
from setuptools import setup, find_packages
__version__ = '1.0.0'

setup(
    name='flaskr',
    version=__version__,
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    dependency_links=[],
    options={"bdist_wheel": {"universal": True}},
    python_requires=">=3.6",
)
# https://realpython.com/python-wheels/
```

`cd flaskr`
`flask run`