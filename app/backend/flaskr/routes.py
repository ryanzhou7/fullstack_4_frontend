# same single app instance 
from flaskr import app
from flaskr.data import get_long_url, save_url
from flask import render_template, request, redirect


@app.route('/<string:short_url>')
def redirect_to(short_url):
    get_long_url(short_url)

    # redirect returns a response which contains a redirect to <url>
    return redirect(f"https://www.google.com/search?q={short_url}")


# Not adding any methods means it is automatically a GET
# but if you add methods, GET must be explicitly added
@app.route('/urls/', methods=('POST', 'GET'))
def urls_fun():
    if request.method == 'POST':
        # Matches the <input/> attribute of the <form/>
        long_url = request.form['long_url']
        print(long_url)

        save_url(long_url)

    # Assumes index.html is in default templates folder, through this can be changed
    return render_template("index.html")
