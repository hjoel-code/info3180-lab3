from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField, TextAreaField, widgets
from wtforms.validators import DataRequired, InputRequired, Email


class ContactForm(FlaskForm):

    name = StringField(name="name", label='Name (Required)', validators=[
                       validators.DataRequired("Your name is required")], description="Please enter your fullname")
    email = StringField(name="email", label='Email (Required)', validators=[validators.DataRequired(
        "Your email is required"), validators.Email("Email is in the incorrect format")], description="Please enter your e-mail address")
    subject = StringField(name="subject", label='Subject (Required)', validators=[
                          validators.DataRequired("A subject is required")], description="Please enter the subject for yout message")
    message = TextAreaField(name="message", label='Message (Required)', validators=[validators.DataRequired("A message is required")] , description="Please enter the email you would like to send")
