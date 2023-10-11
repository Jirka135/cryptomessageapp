from flask import Flask, render_template, request, redirect, url_for,Blueprint

webpage = Blueprint("webpage", __name__)

@webpage.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@webpage.route("/login", methods=['GET','POST'])
def login(status = None):
    username = request.form.get('username')
    password = request.form.get('password')

    # Process the form data, e.g., implement authentication logic
    if username == 'admin' and password == 'admin':
        status = "Login successful"
    else:
        status = "Invalid username or password"

    return render_template('login.html', status=status)


