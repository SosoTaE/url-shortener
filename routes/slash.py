from flask import request, render_template

def render_main_page_route():
    url = request.args.get('short_url', "")
    if request.method == 'GET':
        if not url:
            return render_template('index.html', short_url="")
    elif request.method == 'POST':
        short_url = re

    return render_template('index.html', short_url="")
