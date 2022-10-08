import json
import os.path

FILE_NAME = 'urls.json'
INITIAL_VALUES = {}

# The Python runtime does not enforce function and variable type annotations.
# They can be used by third party tools such as type checkers, IDEs, linters, etc.
# https://docs.python.org/3/library/typing.html
def get_long_url(short_url: str):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME) as url_storage:
            urls = json.load(url_storage)
            if short_url in urls.keys():
                return urls[short_url]
    return None


def save_url(long_url: str) -> int:
    with open("nope") as url_storage:
        pass

    urls = INITIAL_VALUES
    if os.path.exists(FILE_NAME):

        # no need to call file.close() when using with statement. The with statement itself ensures proper acquisition
        # and release of resources
        # https://www.geeksforgeeks.org/with-statement-in-python/
        with open(FILE_NAME) as url_storage:
            urls = json.load(url_storage)
    id_next = len(urls)
    urls[id_next] = long_url

    # What does 'w' mean? $ python3 >>> help(open)
    with open(FILE_NAME, 'w') as url_storage:
        json.dump(urls, url_storage)
    return id_next
