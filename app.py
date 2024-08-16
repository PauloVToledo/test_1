from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/happy", methods=["POST"])
def show_name():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("show_name.html", name=name)
    return redirect("home.html")
