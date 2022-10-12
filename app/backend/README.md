# Url Shortener

## Spec

- Like [tiny url](https://tinyurl.com/app)
- Specifically
  1. Given short url entered in address bar of app -> user redirected to long url in browser
  2. Given long url user wishes to shorten -> user gets short url

## Setup

- There are [environment/tools](https://testdriven.io/blog/python-environments/)
- We use pip + venv
- `bash setup.sh`
- You may have to `chmod +x setup.sh`
  - [chmod cheat sheet](https://quickref.me/chmod)

## Running

- `sh dev.sh`

## Views

- Flask is a full stack framework
- Views are rendered via Jinja and called templates
- **Templates**: files that contain static data as well as placeholders for dynamic data
- {{ and }} is an expression that will be output to the final document. {% and %} denotes a control flow statement like if and for. Between the {} is mostly python
  - [source](https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/)
- This is SSR (server-side rendering)
  - python does not run in the browser
  - Jinja/python does the dynamic replacements then plain .html is returned to

## Routes

- Let's create the endpoints for our app
- Stub out data functions

## Database persistence - json

- Store data in json

## Deployment

- Run this code on another computer
- Sure we could `git clone ... && sh setup.sh && dev.sh` but a distribution file is better
- If someone just wants to run the code, they don't need files like README.md just the app code
- Follows steps [here](https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/)
  - The current standard for Python distribution is the wheel format, with the .whl extension
- `docker pull amazonlinux:2 # Download amazonlinux image tagged with 2 to local`
- `docker container run -dit <IMAGE_ID> # deatached means container will keep running after this command`
- `docker cp backend $CONTAINER_ID:/home`
- `docker exec -it $CONTAINER_ID /bin/bash`
- `yum install python3`
- `ERROR: Could not find a version that satisfies the requirement numpy==1.23.3`

- For dev, setup.sh with requirements.txt worked with hot reload
- For flaskr, pip install . at root directory, cd flaskr, flask run
  - Needed bdist_wheel?
  - pip list only flaskr???