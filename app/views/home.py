from flask import Blueprint, render_template


home = Blueprint("home", __name__)


@home.get("/")
def index():
    return render_template("home/index.html")

@home.get("/about")
def about():
    return "about page"