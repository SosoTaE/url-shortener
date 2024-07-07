from flask import redirect, render_template
from url_shortener import url_shortener
def redirect_route(generated_route):
    real_url_data = url_shortener.get(generated_route)
    if not real_url_data:
        return render_template('index.html', short_url="There is no route to redirect")
    url = real_url_data.get("url")
    return redirect(url)