from flask import Flask
from routes.short_url import get_short_url_route
from routes.slash import render_main_page_route
from routes.redirect import redirect_route

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/api/v1/shorten", methods=["GET", "POST"])
def get_new_short_url():
    return get_short_url_route()

@app.route("/<generated_route>", methods=["GET"])
def redirect(generated_route):
    return redirect_route(generated_route)

@app.route('/', methods=['GET'])
def render_main_page():
    return render_main_page_route()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)