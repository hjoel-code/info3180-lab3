from cProfile import label
from pydoc import classname
from flask_wtf import FlaskForm
from wtforms import StringField, validators, HiddenField, TextAreaField, widgets


class ContactForm(FlaskForm):

    name = StringField(name="name", label='Name', validators=[
                       validators.DataRequired("Your name is required")], description="Please enter your fullname")
    email = StringField(name="email", label='Email', validators=[validators.DataRequired(
        "Your email is required"), validators.Email("Email is in the incorrect format")], description="Please enter your e-mail address")
    subject = StringField(name="subject", label='Subject', validators=[
                          validators.DataRequired("A subject is required")], description="Please enter the subject for yout message")
    message = TextAreaField(name="message", label='Message', validators=[validators.DataRequired("A message is required")] , description="Please enter the email you would like to send")

    token = HiddenField('token')
