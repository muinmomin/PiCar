__author__ = "Muin Momin"

from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from functools import wraps
from controls import *

# Initializing things
app = Flask(__name__)
app.secret_key = "secret"
GPIO.setwarnings(False)
initpins()

error = None


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        global error
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            error = "You need to log in first."
            return redirect(url_for("login"))
    return wrap


#ROUTES FOR PAGES
@app.route("/", methods=["GET", "POST"])
def login():
    global error
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "password":
            error = "Invalid credentials."
        else:
            error = None
            session["logged_in"] = True
            return redirect(url_for("control"))
    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


@app.route("/control")
@login_required
def control():
    user_agent = request.headers.get('user_agent')
    if "Mobile" in user_agent:
        return render_template("touchcontrol.html")
    return render_template("index.html")





#CONTROLLING ELECTRONICS
@app.route("/motorforward", methods=["POST"])
def motor_forward():
    if request.method == "POST":
        forward()
    else:
        return "FAILED"


@app.route("/motorreverse", methods=["POST"])
def motor_reverse():
    if request.method == "POST":
        reverse()
    else:
        return "FAILED"


@app.route("/motorforwardstop", methods=["POST"])
def motor_forward_stop():
    if request.method == "POST":
        stop_forward()
    else:
        return "FAILED"


@app.route("/motorreversestop", methods=["POST"])
def motor_reverse_stop():
    if request.method == "POST":
        stop_reverse()
    else:
        return "FAILED"


@app.route("/turnleft", methods=["POST"])
def motorleft():
    if request.method == "POST":
        left()
    else:
        return "FAILED"

@app.route("/turnright", methods=["POST"])
def motorright():
    if request.method == "POST":
        right()
    else:
        return "FAILED"

@app.route("/stopleft", methods=["POST"])
def stopmotorleft():
    if request.method == "POST":
        stop_left()
    else:
        return "FAILED"

@app.route("/stopright", methods=["POST"])
def stopmotorright():
    if request.method == "POST":
        stop_right()
    else:
        return "FAILED"







@app.route("/flashled", methods=["POST"])
def power_led():
    if request.method == "POST":
        powerled()
    else:
        return "FAILED"

@app.route("/distance", methods=["GET"])
def calculate_distance():
    d = "%.2f" % distance()
    return jsonify(dist=d)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    initpins()