from flask import Blueprint, request
from flask import Blueprint, render_template, redirect, url_for, request # New imports added


post_pages = Blueprint("posts", __name__)


@post_pages.get("/post/<string:title>")
def display_post(title: str):
    return "Display post page."


@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        pass
    return "Create post page."

@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        # TODO: We can create the post in our database here
        return redirect(url_for(".display_post", title=title))
    return render_template("new_post.html")

@post_pages.get("/post/<string:title>")
def display_post(title):
    content = "..." # How do we get the content?
    return render_template("post.html", title=title, content=content)