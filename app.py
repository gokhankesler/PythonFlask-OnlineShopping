from flask import (Flask, render_template, request, redirect,
                   url_for, g)
import sqlite3

# import pdb
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/item/new", methods=['GET', 'POST'])
def new_item():
    if request.method == "POST":
        print("Form Data:")
        print(f"Title: {request.form['title']}, Description: {request.form['description']}")

        # Redirect to some page
        return redirect(url_for("home"))
    return render_template("new_item.html")


def get_db():
    db = getattr(g, "_database", None)
    g._database = sqlite3.connect("db/globomantics.db")
