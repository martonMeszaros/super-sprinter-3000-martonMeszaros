"""."""
# Refactor sloppy bits of code.
from flask import Flask, render_template, redirect, request, url_for

from data_manager import get_new_id, get_table, save_table,\
    update_story, del_story

app = Flask(__name__)


@app.route("/list")
@app.route("/")
def index():
    """Render a table of the existing stories."""
    title = "Super Sprinter 3000"
    h1 = "User Story Manager"
    table = get_table()
    return render_template(
        "list.html",
        title=title, h1=h1, table=table
    )


@app.route("/story")
def new_story():
    """Create a new story."""
    title = "Super Sprinter 3000 - Add new Story"
    h1 = "User Story Manager - Add new Story"
    entry = [False] * 7
    entry[0] = get_new_id()
    return render_template(
        "form.html",
        title=title, h1=h1, entry=entry
    )


@app.route("/story/<int:story_id>")
def edit_story(story_id=None):
    """Edit an existing story."""
    title = "Super Sprinter 3000 - Edit Story"
    h1 = "User Story Manager - Edit Story"
    # Select the story from the table based on it's ID.
    for row in get_table():
        if row[0] == story_id:
            entry = row
            break
    return render_template(
        "form.html",
        title=title, h1=h1, entry=entry
    )


@app.route("/process/<int:story_id>/<action>", methods=["POST", "GET"])
def process(action=False, story_id=None):
    """Process actions. Either creating, editing or deleting a story."""
    if action:
        table = get_table()
        if not table:
            table = []
        # Link came from new_story() or edit_story().
        if request.method == "POST":
            story = [
                request.form["id"],
                request.form["story_title"],
                request.form["user_story"],
                request.form["acceptance_criteria"],
                request.form["buisness_value"],
                request.form["estimation"],
                request.form["status"]
            ]
            if action == "new":
                table.append(story)
            elif action == "edit":
                table = update_story(table, story)
        # Link came from index().
        elif request.method == "GET":
            if action == "delete" and story_id:
                table = del_story(table, story_id)
        save_table(table)
    # Redirect to index page.
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    """Display custom error page when requesting non-existent page."""
    return render_template("error/404.html"), 404


if __name__ == "__main__":
    app.run("0.0.0.0")
