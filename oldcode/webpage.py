from flask import Flask, render_template, request, redirect, url_for,Blueprint,jsonify

webpage = Blueprint("webpage", __name__)

@webpage.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@webpage.route("/login", methods=['GET','POST'])
def login(status = None):
    user_login = {
        "jmeno":request.form.get('username'),
        "hashedpassword":request.form.get('password')
    }
    jsonify(user_login),200
    status = ""
    # Process the form data, e.g., implement authentication logic
   

    return render_template('login.html', status=status)


