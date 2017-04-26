from flask import Flask, render_template, redirect, request, url_for

import process_data
app = Flask(__name__)


@app.route("/list")
@app.route("/")
def index():
    title = "Super Sprinter 3000"
    h1 = "User Story Manager"
    table = process_data.get_table()
    return render_template(
        "list.html",
        title=title, h1=h1, table=table
    )


@app.route("/story")
def new_story():
    title = "Super Sprinter 3000 - Add new Story"
    h1 = "User Story Manager - Add new Story"
    entry = [False] * 7
    entry[0] = process_data.get_new_id()
    return render_template(
        "form.html",
        title=title, h1=h1, entry=entry
    )


@app.route("/story/<int:story_id>")
def edit_story(story_id=None):
    title = "Super Sprinter 3000 - Edit Story"
    h1 = "User Story Manager - Edit Story"
    for row in process_data.get_table():
        if row[0] == story_id:
            entry = row
            break
    return render_template(
        "form.html",
        title=title, h1=h1, entry=entry
    )


@app.route("/process<action><int:story_id>", methods=["POST", "GET"])
def process(action=False, story_id=None):
    if action:
        table = process_data.get_table()
        if not table:
            table = []
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
                table = process_data.update_story(table, story)
        elif request.method == "GET":
            if action == "delete" and story_id:
                table = process_data.del_story(table, story_id)
        process_data.save_table(table)
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404


if __name__ == "__main__":
    app.run()
