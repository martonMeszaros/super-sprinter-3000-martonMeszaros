from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)


@app.route("/list")
@app.route("/")
def index():
    title = "Super Sprinter 3000"
    h1 = "User Story Manager"
    table = False
    return render_template(
        "list.html",
        title=title, h1=h1, table=table
    )


@app.route("/story")
def new_entry():
    title = "Super Sprinter 3000 - Add new Story"
    h1 = "User Story Manager - Add new Story"
    entry = [False] * 7
    entry[0] = 1
    return render_template(
        "form.html",
        title=title, h1=h1, entry=entry
    )


@app.route("/story/<int:story_id>")
def edit_entry():
    title = "Super Sprinter 3000 - Edit Story"
    h1 = "User Story Manager - Edit Story"
    return redirect(url_for("index"))


@app.route("/process", methods=["POST"])
def process(action="new"):
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404


if __name__ == "__main__":
    app.run()
