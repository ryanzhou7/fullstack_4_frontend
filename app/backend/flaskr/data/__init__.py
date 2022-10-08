import json
import os.path
from typing import Dict

FILE_NAME = 'urls.json'
INITIAL_VALUES = {}


# The Python runtime does not enforce function and variable type annotations.
# They can be used by third party tools such as type checkers, IDEs, linters, etc.
# https://docs.python.org/3/library/typing.html
def get_long_url(url_id: str):
    urls = get_urls()
    if url_id in urls.keys():
        return urls[url_id]


def save_url(long_url: str) -> int:
    urls = get_urls()
    curr_id = len(urls)
    urls[str(curr_id)] = long_url
    # whats the significance of 'w'? $ python3 >>> help(open)
    with open(FILE_NAME, 'w') as url_storage:
        json.dump(urls, url_storage)
    return curr_id


def get_urls() -> Dict[str, str]:
    """ Returns all stored URLS """
    if not os.path.exists(FILE_NAME):
        return INITIAL_VALUES

    # no need to call file.close() when using with statement. The with statement itself ensures proper acquisition
    # and release of resources
    # https://www.geeksforgeeks.org/with-statement-in-python/
    with open(FILE_NAME) as url_storage:
        # turns it into python obj
        return json.load(url_storage)
