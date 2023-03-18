from flask import Flask, render_template, redirect, url_for

# set the project root directory as the static folder, you can set others.

# Create a Flask Instance, that will let the application find all the files and directories
app = Flask(__name__)

# Create a route decorator, to browse the files and foldersin the directory and have an access to it.
app.errorhandler(404)


def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/user/<name>')
def user(name):
    return "<h1> Hello {} </h1>".format(name)
