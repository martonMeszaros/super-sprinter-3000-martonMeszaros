from flask import Flask, render_template, request, url_for
app = Flask(__name__)


@app.route("/list")
@app.route("/")
def index():
    return "Index"


@app.errorhandler(404)
def page_not_found(error):
    return "Page not found!", 404


if __name__ = "__main__":
    app.run()
