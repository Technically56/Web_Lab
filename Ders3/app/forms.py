from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class ForgetPasswordForm(FlaskForm):
    mail = StringField("Mail", validators=[DataRequired()])

    submit = SubmitField("Send Mail")


class LoginFeedbackForm(FlaskForm):
    feedback = StringField("Feedback", validators=[DataRequired()])

    name = StringField("Name", validators=[DataRequired()])

    email = StringField("Email", validators=[DataRequired()])

    submit = SubmitField("Submit Feedback")
