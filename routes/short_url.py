from flask import request, Response, redirect, url_for, render_template
from url_shortener import URlShortener
from tools import is_valid_url
from url_shortener import url_shortener



def get_short_url_route():
    url = request.args.get("url", "")
    if not url or not is_valid_url(url):
        return render_template("index.html", short_url="URL is not valid")

    short_url = url_shortener.get_new_short_url(url)
    origin = request.host_url
    return render_template("index.html", short_url=origin + short_url)
