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
