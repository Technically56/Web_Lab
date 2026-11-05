import os

from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import ForgetPasswordForm, LoginFeedbackForm, LoginForm


@app.route("/")
@app.route("/index")
@app.route("/index/<username>")
def index(username=None):
    user = {"username": username or "John Doe"}
    return render_template("index.html", title="Home", user=user, posts=[])


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/forget_password", methods=["GET", "POST"])
def forget_password():
    form = ForgetPasswordForm()
    if form.validate_on_submit():
        return redirect(url_for("login"))
    return render_template("forget_password.html", title="Forget Password", form=form)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login_feedback", methods=["GET", "POST"])
def login_feedback():
    form = LoginFeedbackForm()
    if form.validate_on_submit():
        flash(f"Feedback submitted by {form.name.data}, email={form.email.data}")
        feedback_path = os.path.join(app.root_path, "feedback.txt")
        with open(feedback_path, "a", encoding="utf-8") as f:
            f.write(
                f"Feedback: {form.feedback.data}\nName: {form.name.data}\nEmail: {form.email.data}\n\n"
            )
        return redirect(url_for("index"))

    return render_template("feedback.html", title="Feedback", form=form)
